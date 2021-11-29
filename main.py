from os import name
from flask import Flask, request, jsonify
from sqlalchemy.sql.expression import text
import tools.main_tools as mt
import random
from tools.main_tools import personajes


app = Flask(__name__)

@app.route("/")
def inicio():
    return "The office"


@app.route("/personajes")
def speakers():
    persons = mt.personajes()
    return jsonify(persons)

@app.route("/frases/<name>")
def quotes_names(name):
    frases = f"{name} says {mt.quotes(name)[0]}"
    return jsonify(frases)

@app.route("/frase/<episodio>")
def quotes_episode(episodio):
    frases = mt.episodios(episodio)
    return jsonify(frases)

@app.route("/nuevafrase", methods=["POST"])
def insertamensaje():
    episodio = request.form.get("episode")
    personaje = request.form.get("speaker")
    texto = request.form.get("text")

    print(episodio, personaje, texto)

    return mt.nuevomensaje(episodio,personaje,texto)

@app.route("/borrafrase",  methods=["POST"])
def borrar():
    return mt.borramensaje(text)














app.run(debug=True)