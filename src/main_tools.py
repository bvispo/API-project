from configuration.configuration import engine
import pandas as pd

def personajes():
    query = list(engine.execute("SELECT distinct(speaker_name) FROM api.speaker;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista

def text(personaje):
    query = f"""
    SELECT text 
    FROM api.text 
    WHERE speaker_idpseaker = '{personaje}';
    """