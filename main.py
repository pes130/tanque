from flask import Flask, jsonify
import logging
import os
import constantes as ctes
import robotControlador


# Iniciamos fichero de logs
if not os.path.isdir(ctes.LOGS_RUTA):
    os.makedirs(ctes.LOGS_RUTA)
fichero_log = ctes.LOGS_RUTA + "/" + ctes.LOGS_FICHERO
logging.basicConfig(filename=fichero_log,level=logging.DEBUG)

app = Flask(__name__)
rc = robotControlador.RobotControlador()

@app.route('/')
def hello_world():
    return 'Funciono!!'

@app.route('/name', methods=['GET'])
def name():
    return jsonify(rc.nombre()), 200

@app.route('/mvmto/avanzar')
def avanzar():
    return jsonify(rc.adelante()), 200

@app.route('/mvmto/parar')
def parar():
    return jsonify(rc.parar()), 200

@app.route('/mvmto/atras')
def atras():
    return jsonify(rc.atras()), 200

@app.route('/mvmto/izquierda')
def izquierda():
    return jsonify(rc.izquierda()), 200

@app.route('/mvmto/izquierdax')
def izquierdax():
    return jsonify(rc.izquierdax()), 200

@app.route('/mvmto/derecha')
def derecha():
    return jsonify(rc.derecha()), 200

@app.route('/mvmto/derechax')
def derechax():
    return jsonify(rc.derechax()), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')