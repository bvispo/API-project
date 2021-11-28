from configuration.configuration import engine
import pandas as pd

def personajes():
    query = list(engine.execute("SELECT distinct(speaker_name) FROM api.speaker;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista

def quotes(personaje):
    person = list(engine.execute(f"SELECT idspeaker FROM api.speaker WHERE speaker_name = '{personaje}' ;"))[0][0]
    what = list(engine.execute(f"SELECT text FROM text WHERE speaker_idspeaker = '{person}';"))
    return what

def episodios (episodio):
    episode = list(engine.execute(f"SELECT idepisode from api.episode WHERE episode_name = '{episodio}'"))
    what = list(engine.execute(f"SELECT text FROM text WHERE episode_idepisode = '{episode}';"))
    return episode