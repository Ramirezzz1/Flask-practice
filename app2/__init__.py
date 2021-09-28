#flask object and config class
from flask import Flask 
from config import Config 

from .movies.routes import movies 

app2 = Flask(__name__)

app2.register_blueprint(movies)

app2.config.from_object(Config)

from . import routes 