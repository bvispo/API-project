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
def frases(name):
    frases = mt.text(name)
    return jsonify(frases)
























app.run(debug=True)