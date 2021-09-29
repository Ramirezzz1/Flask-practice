#flask object and config class
from flask import Flask 
from config import Config 

from .movies.routes import movies 

from .models import db
from flask_migrate import Migrate, migrate

app2 = Flask(__name__)

app2.register_blueprint(movies)

app2.config.from_object(Config)

db.init_app(app2)

migrate = Migrate(app2,db)   

from . import routes 
from . import models
