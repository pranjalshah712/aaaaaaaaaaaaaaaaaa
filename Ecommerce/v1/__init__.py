from Ecommerce import app, api
from flask import Blueprint
from Ecommerce.v1 import endpoints

blueprint = Blueprint('Ecommerce', __name__)
api.blueprint = blueprint
api.blueprint_setup = blueprint

app.register_blueprint(blueprint)
