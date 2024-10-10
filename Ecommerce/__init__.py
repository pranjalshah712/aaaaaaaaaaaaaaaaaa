from flask import Flask
from flask_restful import Api

import importlib

app = Flask(__name__, template_folder='../template', static_folder='../static')
api = Api(app)
app.secret_key = 'secretksyforevreyteff0'

importlib.import_module('Ecommerce.v1')
