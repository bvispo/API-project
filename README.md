# API-project


The objetive of this project is to create our own API trough web-scrapping and querying databases for data.

In order to get the data, I have used a Kaggle dataset that compiles the script from the 9 seasons of the tv show The office.
Data available at: [The office Database](https://www.kaggle.com/nehaprabhavalkar/the-office-dataset)

## The API

### Overview:
Welcome to The Office API. Using this service, you can get the main characters of the tv show, some random quotes of the characters and a random quote in a given episode. Moreover, the API also lets you create some new quotes for the alredy existing characters and also delate some og the quotes.

### Authentication
Currently there is no authentication needed. You just need to establish the connection to the sql database.

### ENDPOINTS .GET

1. personajes
This endpoint returns a json containing the main characters of the show.
Example Resource URL: http://127.0.0.1:5000/personajes
Example Response:
[
  {
    "nombre": "Jim"
  }, 
  {
    "nombre": "Dwight"
  }, 
  {
    "nombre": "Michael"
  }, 
  {
    "nombre": "Pam"
  }
]

2. frases/<name>
This endpoint returns random quotes of a given character.
Example Resource URL: http://127.0.0.1:5000/frases/Pam
Example Response:
"Pam says ('Yeah`turn signal. It`s exciting to be painting again`those are the wipers. So`the`its`just. There you go! Yeah. [chuckles]  Yeah, things get so busy with the kids`red light`that it`s nice to have that creative outlet`red light! Red light! Red! Red!',)"

3. frase/<episodio>
This endpoint returns a random quote of a given episode.
Example Resource URL: http://127.0.0.1:5000/frase/4x6
Example Response:
'La frase del capítulo 4x6': 'My hip bone!'

### ENDPOINT .POST:

1. nuevafrase
This endpoint creates a new quote for an existent character in de sql database.
It needs to recive the data in a dicctionary. 
- Example: insertar = {"episode": 1, "speaker":3, "text": "Hello"}
Example Resource URL: http://127.0.0.1:5000/nuevafrase

2. borrafrase
This endpoint delates a quote from the sql database.
- Example: text = "Hello"
Example Resource URL: http://127.0.0.1:5000/borrafrase


## Libraries
[import requests](https://pypi.org/project/requests/2.7.0/)

[import pandas as pd](https://pandas.pydata.org/)

[import numpy as np](https://numpy.org/doc/)

[import flask](https://flask.palletsprojects.com/en/2.0.x/)

[import random](https://docs.python.org/3/library/random.html)

[import sqlalchemy](https://docs.sqlalchemy.org/en/14/)

[import sys](https://docs.python.org/3/library/sys.html)

[import spacy](https://spacy.io/api/doc)