from os import name
from flask import Flask, request, jsonify
import src.main_tools as mt


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

@app.route("/frase/<episode>")
def quotes_episode(quote):
    frases = f"In {quote} is this quote: {mt.episodios(quote)}"
    return jsonify(frases)
























app.run(debug=True)