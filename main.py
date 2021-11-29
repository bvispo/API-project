from os import name
from flask import Flask, request, jsonify
import src.main_tools as mt
import random

from src.tools.main_tools import personajes


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

@app.route("/nuevafrase/<episode>/<speaker>/<text>", methods=["POST"])
def insertamensaje():
    episodio = request.form.get("episode")
    personaje = request.form.get("speaker")
    texto = request.form.get("text")
    # PODRÍAMOS LLAMAR A FUNCIONES CHECK
    print(episodio, personaje, texto)

    return mt.nuevomensaje(episodio,personaje,texto)























app.run(debug=True)