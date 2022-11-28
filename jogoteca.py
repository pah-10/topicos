from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

#Instanciando a ponte do banco do SQLALCHEMY com o real
db = SQLAlchemy(app)

#Carregamento da Imagem da logo
IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

#Chamada as rotas com as views/telas
from views import *

if __name__ == '__main__':
    app.run(debug=True)