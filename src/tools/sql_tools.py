import pandas as pd
import dotenv
import os
import sqlalchemy as alch
from getpass import getpass

import sys
sys.path.append('../')

from src.config.configuration import engine 


def sustituye(x):
    x = str(x).replace('"', "`")
    x = str(x).replace("'", "`")
    return x


def check(que,string):
    """
    Función parametrizada que comprueba en cada tabla si existe el speaker, episodio.
    Devuelve True si existe y False si no
    """
    if que == "speaker": #nombre columna df
        query = list(engine.execute(f"SELECT speaker_name FROM speaker WHERE speaker_name = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif que == "episodio": #nombre columna df
        query = list(engine.execute(f"SELECT episode_name FROM episode WHERE episode_name = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
    
    elif que == "line_text": #nombre columna df
        query = list(engine.execute(f"SELECT text FROM text WHERE text = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False  

def insertSpeaker(lista):
    """
    Esta función recibe una lista de strings
    Llama a la función check para comprobar si existe el speaker
    Inserta ironhacker si no existe
    """
    for i in lista:
        if check("speaker", i):
            return "el speaker existe"
        else:
            engine.execute(f"INSERT INTO speaker (speaker_name) VALUES ('{i}');")


def insertEpisode(lista):
    """
    Esta función recibe una lista de strings
    Llama a la función check para comprobar si existe el episodio
    Inserta ironhacker si no existe
    """
    for i in lista:
        if check("episodio", i):
            return "el episode existe"
        else:
            engine.execute(f"INSERT INTO episode (episode_name) VALUES ('{i}');")


def dameId(que,string):
    """
    Devuelve el ID de lo que le pidamos sabiendo que ese elemento EXISTE
    """
    if que == "speaker":
        return list(engine.execute(f"SELECT idspeaker FROM speaker WHERE speaker_name ='{string}';"))[0][0]
    elif que == "episode":
        return list(engine.execute(f"SELECT idepisode FROM episode WHERE episode_name ='{string}';"))[0][0]


def insertText(df):
    """
    La función final, inserta las frases.
    """
    if check("line_text", df["line_text"]):
        return "la frase ya existe"
    else:
        if check("speaker", df["speaker"]):
            speaker_id = dameId("speaker", df["speaker"])
        else:
            insertSpeaker(df["speaker"])
            speaker_id = dameId("speaker", df["speaker"])
        
        if check("episode", df["episodio"]):
            episode_id = dameId("episode", df["episodio"])
        else:
            insertEpisode(df["episodio"])
            episode_id = dameId("episode", df["episodio"])
        
        engine.execute(f"""
        INSERT INTO text (text, speaker_idspeaker, episode_idepisode) VALUES
        ("{df['line_text']}", {speaker_id}, {episode_id});
        """)