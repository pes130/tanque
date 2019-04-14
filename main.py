from flask import Flask
import logging
import os
import constantes as ctes


# Iniciamos fichero de logs
if not os.path.isdir(ctes.LOGS_RUTA):
    os.makedirs(ctes.LOGS_RUTA)
fichero_log = ctes.LOGS_RUTA + "/" + ctes.LOGS_FICHERO
logging.basicConfig(filename=fichero_log,level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Funciono!!'
