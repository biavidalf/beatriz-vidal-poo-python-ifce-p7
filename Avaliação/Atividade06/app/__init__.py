from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# from models import cliente
from Avaliação.Atividade06.app import controller
from Avaliação.Atividade06.app.controller import rotas