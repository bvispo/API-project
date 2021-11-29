from config.configuration import engine
import pandas as pd
import random
import spacy
import en_core_web_sm
from nltk.corpus import stopwords
import re
from textblob import TextBlob
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# ENDPOINTS GET:

def personajes():
    """
    This funcion returns a list with the characters names.
    """
    query = list(engine.execute("SELECT distinct(speaker_name) FROM api.speaker;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista


def quotes(personaje):
    """
    This funcion returns a random quote of a given characters.
    """
    person = list(engine.execute(f"SELECT idspeaker FROM api.speaker WHERE speaker_name = '{personaje}' ;"))[0][0]
    what = list(engine.execute(f"SELECT text FROM text WHERE speaker_idspeaker = '{person}';"))
    return random.choices(what)


def episodios(episodio):
    """
    This funcion returns a quote of a given episode.
    """
    frase = random.choice(list(engine.execute(f"""
    SELECT text 
    FROM text
    INNER JOIN api.episode
    ON episode.idepisode = text.episode_idepisode
    WHERE episode_name = '{episodio}'
    """)))[0]

    return {f"La frase del capítulo {episodio}": frase}


# ENDPOINTS POST:

def nuevomensaje(episode,speaker,text):
    """
    This funcion posts a new quote for an already existen character.
    Arggs: a dictionaty with the required values: episode, speaker, text.
    """
    engine.execute(f"""
    INSERT INTO text (episode_idepisode, speaker_idspeaker,text)
    VALUES ({episode}, {speaker}, '{text}');
    """)
    
    return f"Se ha introducido correctamente: {episode} {speaker} {text}"


def borramensaje(text):
    """
    This funcion delates a quote from the sql database.
    Arggs: a variable with the quote to be delated.
    """
    engine.execute(f"""
    SELECT text FROM api.text WHERE text= '{text}';""")
    
    engine.execute(f"""
    DELETE FROM api.text where text= '{text}';""")

    return "The text has been deleted"


# ENDPOINTS SENTIMENTAL ANALYSIS:

def analisis_sentimientos(speaker):
    """
    This gets all quotes from a given character.
    Arggs: the speaker name.
    """

    query = f"""
    SELECT text.text
    FROM api.text
    INNER JOIN api.speaker
    ON speaker.idspeaker = text.speaker_idspeaker
    WHERE speaker_name = '{speaker}';
    """
    data = pd.read_sql_query(query, engine)
    return data


def tokenizer(texto):
    """
    This function recieves a df and takes out from it the stopwords in english. 
    It also replaces the suffixes of the words to leave them at the root.
    Arggs: data frame
    Returns: string with the root of the given words.    
    """

    nlp = spacy.load("en_core_web_sm")
    stop = nlp.Defaults.stop_words
    tokens = nlp(texto)
    filter = []
    for i in tokens:
        if not i.is_stop:
            lemma = i.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma):
                filter.append(lemma)
    return " ".join(filter)


def sentiment(phrases):
    sia = SentimentIntensityAnalyzer()
    polaridad = sia.polarity_scores(phrases)
    pol = polaridad["compound"]
    return pol