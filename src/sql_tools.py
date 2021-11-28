import pandas as pd
import sqlalchemy as alch
from getpass import getpass
from configuration.configuration import engine

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

def insertSpeaker(string):
    """
    Llama a la función check para comprobar si existe el speaker
    Inserta speaker si no existe
    """
    if check("speaker", string):
        return "el speaker existe"
    else:
        engine.execute(f"INSERT INTO speaker (speaker_name) VALUES ('{string}');")


def insertEpisode(string):
    """
    Llama a la función check para comprobar si existe el episodio
    Inserta episodio si no existe
    """
    if check("episodio", string):
        return "el episode existe"
    else:
        engine.execute(f"INSERT INTO episode (episode_name) VALUES ('{string}');")


def dameId(que,string):
    """
    Devuelve el ID de lo que le pidamos sabiendo que ese elemento EXISTE
    """
    if que == "speaker":
        return list(engine.execute(f"SELECT idspeaker FROM speaker WHERE speaker_name ='{string}';"))[0][0]
    elif que == "episode":
        return list(engine.execute(f"SELECT idepisode FROM episode WHERE episode_name ='{string}';"))[0][0]