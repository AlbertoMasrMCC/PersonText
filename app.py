from flask import Flask
from flask_cors import CORS, cross_origin  #Para poder atender las peticiones localmente
from flask import jsonify
from persontext import predict_personalidad
import os

app = Flask(__name__)

#Para poder atender las peticiones locales
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

APP_ROOT=os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    """
    Página inicial
    """
    return "<h1>Bienvenidos a ApiPersonText v0.12<h1>"

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/persontext/apertura/<texto>',methods=["GET","POST"])
@cross_origin() #Para poder atender las peticiones locales
def persontext_apertura(texto):
    datos = {}
    prediccion = predict_personalidad("apertura", texto.lower())
    datos["presenta_personalidad"] = prediccion
    return jsonify(datos)

@app.route('/persontext/responsabilidad/<texto>',methods=["GET","POST"])
@cross_origin() #Para poder atender las peticiones locales
def persontext_responsabilidad(texto):
    datos = {}
    prediccion = predict_personalidad("responsabilidad", texto.lower())
    datos["presenta_personalidad"] = prediccion
    return jsonify(datos)

@app.route('/persontext/sociabilidad/<texto>',methods=["GET","POST"])
@cross_origin() #Para poder atender las peticiones locales
def persontext_sociabilidad(texto):
    datos = {}
    prediccion = predict_personalidad("sociabilidad", texto.lower())
    datos["presenta_personalidad"] = prediccion
    return jsonify(datos)

@app.route('/persontext/amabilidad/<texto>',methods=["GET","POST"])
@cross_origin() #Para poder atender las peticiones locales
def persontext_amabilidad(texto):
    datos = {}
    prediccion = predict_personalidad("amabilidad", texto.lower())
    datos["presenta_personalidad"] = prediccion
    return jsonify(datos)

@app.route('/persontext/neuroticismo/<texto>',methods=["GET","POST"])
@cross_origin() #Para poder atender las peticiones locales
def persontext_neuroticismo(texto):
    datos = {}
    prediccion = predict_personalidad("neuroticismo", texto.lower())
    datos["presenta_personalidad"] = prediccion
    return jsonify(datos)

if __name__ == "__main__":
   app.run() ##Replaced with below code to run it using waitress 
   #serve(app, host='0.0.0.0', port=5000, url_scheme='https')