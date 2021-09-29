import os 
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY

basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    """
    Set my configuration variables 
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATE_URI')
    SQLALCHEMY_TRACK_MODIFICATION = False
#         def new_func():
#     SECRET_KEY = os.environ.get('SECRET_KEY')

# new_func()