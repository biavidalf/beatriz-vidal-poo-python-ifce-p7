from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# from models import cliente
from app.controllers import rotas
