# API-project
![foto](https://github.com/bvispo/API-project/blob/main/images/the-office.jpg)

The objetive of this project is to create our own API trough web-scrapping and querying databases for data.

In order to get the data, I have used a Kaggle dataset that compiles the script from the 9 seasons of the tv show The office.
- Data available at: [The Office Database](https://www.kaggle.com/nehaprabhavalkar/the-office-dataset)

## The API

### Overview:
Welcome to The Office API. Using this service, you can get the main characters of the tv show, some random quotes of the characters and a random quote in a given episode. Moreover, the API also lets you create some new quotes for the alredy existing characters and also delate some og the quotes.

### Authentication
Currently there is no authentication needed. You just need to establish the connection to the sql database.

### Starting the API
```
resource_URL = http://127.0.0.1:5000/
```
- Expected response: Welcome to The Office Show API.

### ENDPOINTS GET

1. /personajes

This endpoint returns a json containing the main characters of the show.
```
url = http://127.0.0.1:5000/personajes
```
- Example Response:
```
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
```

2. /frases/<name>

This endpoint returns random quotes of a given character.
```
user = Pam
url= "http://127.0.0.1:5000/frases/user"
requests.get(url, user)
```
- Example Response: "Pam says ('We can do that.')"


3. /frase/<episodio>

This endpoint returns a random quote of a given episode.
```
episode = 4x6
url = "http://127.0.0.1:5000/frase/episode"
requests.get(url, episode)
```
- Example Response: 'La frase del capítulo 4x6': 'My hip bone!'

### ENDPOINT POST:

1. /nuevafrase

This endpoint creates a new quote for an existent character in de sql database.
It needs to recive the data from a dicctionary.
You can insert a quote like this:
```
insertar = {"episode": 1, "speaker":3, "text": "hello"}
url_nueva_frase = "http://127.0.0.1:5000/nuevafrase"
requests.post(url_nuevafrase, data=insertar)
```

2. /borrafrase

This endpoint delates a quote from the sql database.
You can delate a quote like this:
```
text_to_delate = "Hello
url_delate = "http://127.0.0.1:5000/borrafrase"
requests.post(url_delate, data=text_to_delate)
```

### ENDPOINT SENTIMENTAL ANALYSIS:

1. /sentimientos/<name>

This endpoint makes a sentiment analysis, taking all the quotes of a given character in the tv show.
```
user = Pam
url = "http://127.0.0.1:5000/sentimientos/user"
requests.get(url, user)
```
- Example Response for Pam: 0.18761301369863015


## Libraries
[import requests](https://pypi.org/project/requests/2.7.0/)

[import pandas as pd](https://pandas.pydata.org/)

[import numpy as np](https://numpy.org/doc/)

[import flask](https://flask.palletsprojects.com/en/2.0.x/)

[import random](https://docs.python.org/3/library/random.html)

[import sqlalchemy](https://docs.sqlalchemy.org/en/14/)

[import sys](https://docs.python.org/3/library/sys.html)

[import spacy](https://spacy.io/api/doc)

[import nltk](https://www.nltk.org/)