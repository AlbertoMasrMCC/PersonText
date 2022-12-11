import numpy as np
import tensorflow as tf
import json
import keras
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

# Creamos la lista de clases
clases = ['No','Si']

modelo_personalidad_apertura        = tf.keras.models.load_model("PersonText_Apertura.h5")
modelo_personalidad_responsabilidad = tf.keras.models.load_model("PersonText_Responsabilidad.h5")
modelo_personalidad_sociabilidad    = tf.keras.models.load_model("PersonText_Sociabilidad.h5")
modelo_personalidad_amabilidad      = tf.keras.models.load_model("PersonText_Amabilidad.h5")
modelo_personalidad_neuroticismo    = tf.keras.models.load_model("PersonText_Neuroticismo.h5")

def crear_tokenizer():
    f = open('datos_dicc.json')
    # returns JSON object as a dictionary
    datos_dicc2 = json.load(f)
    datos_dicc2 = json.dumps(datos_dicc2)
    tokenizer = keras.preprocessing.text.tokenizer_from_json(datos_dicc2)
    return tokenizer

def predict_personalidad(personalidad, texto):

    if personalidad == "apertura":
        modelo_personalidad = modelo_personalidad_apertura
    elif personalidad == "responsabilidad":
        modelo_personalidad = modelo_personalidad_responsabilidad
    elif personalidad == "sociabilidad":
        modelo_personalidad = modelo_personalidad_sociabilidad
    elif personalidad == "amabilidad":
        modelo_personalidad = modelo_personalidad_amabilidad
    elif personalidad == "neuroticismo":
        modelo_personalidad = modelo_personalidad_neuroticismo

    tokenizer = crear_tokenizer()
    word_index = tokenizer.word_index
    total_unique_words = len(tokenizer.word_index) + 1
    max_words = total_unique_words
    max_len = 193 #max_seq_length
    sequence = tokenizer.texts_to_sequences([texto])
    test = pad_sequences(sequence, maxlen=max_len)
    return clases[np.around(modelo_personalidad.predict(test), decimals=0).argmax(axis=1)[0]]