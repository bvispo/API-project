from config.configuration import engine
import pandas as pd
import random

def personajes():
    query = list(engine.execute("SELECT distinct(speaker_name) FROM api.speaker;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista

def quotes(personaje):
    person = list(engine.execute(f"SELECT idspeaker FROM api.speaker WHERE speaker_name = '{personaje}' ;"))[0][0]
    what = list(engine.execute(f"SELECT text FROM text WHERE speaker_idspeaker = '{person}';"))
    return what

def episodios(episodio):
    frase = random.choice(list(engine.execute(f"""
    SELECT text 
    FROM text
    INNER JOIN api.episode
    ON episode.idepisode = text.episode_idepisode
    WHERE episode_name = '{episodio}'
    """)))[0]

    return {f"La frase del capítulo {episodio}": frase}


def nuevomensaje(episode,speaker,text):
    engine.execute(f"""
    INSERT INTO text (episode_idepisode, speaker_idspeaker,text)
    VALUES ({episode}, {speaker}, '{text}');
    """)
    
    return f"Se ha introducido correctamente: {episode} {speaker} {text}"


def borramensaje(text):
    engine.execute(f"""
    SELECT text FROM api.text WHERE text= '{text}';""")
    
    engine.execute(f"""
    DELETE FROM api.text where text= '{text}';""")

    return "The text has been deleted"

