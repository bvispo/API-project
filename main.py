from os import name
from flask import Flask, request, jsonify
from sqlalchemy.sql.expression import text
import tools.main_tools as mt
from tools.main_tools import personajes


app = Flask(__name__)

# START
@app.route("/")
def inicio():
    """
    This function initializes the API.
    """
    return "Welcome to The Office Show API"

# ENDPOINTS GET:

@app.route("/personajes")
def speakers():
    """
    This function gets all the characters.
    """
    persons = mt.personajes()
    return jsonify(persons)

@app.route("/frases/<name>")
def quotes_names(name):
    """
    This function gets a random quote from a given character.
    """
    frases = f"{name} says {mt.quotes(name)[0]}"
    return jsonify(frases)

@app.route("/frase/<episodio>")
def quotes_episode(episodio):
    """
    This function gets a random quote from a given episode.
    """
    frases = mt.episodios(episodio)
    return jsonify(frases)


# ENDPOINTS POST:

@app.route("/nuevafrase", methods=["POST"])
def insertamensaje():
    """
    This funcion posts a new quote for an already existen character.
    """
    episodio = request.form.get("episode")
    personaje = request.form.get("speaker")
    texto = request.form.get("text")

    print(episodio, personaje, texto)

    return mt.nuevomensaje(episodio,personaje,texto)

@app.route("/borrafrase", methods=["POST"])
def borrar():
    """
    This funcion delates a quote from the sql database.
    """
    texto = request.form.get("text")
    return mt.borramensaje(texto)


# ENDPOINTS SENTIMENTAL ANALYSIS:

@app.route("/sentimientos/<name>")
def sentimientos(name):
    df= mt.analisis_sentimientos(name)
    df["phrases_token"] = df["text"].apply(mt.tokenizer)
    df["resultado"] = df["phrases_token"].apply(mt.sentiment)
    print (df.resultado)
    return str(df.resultado.mean())


app.run(debug=True)