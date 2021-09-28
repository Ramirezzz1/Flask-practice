import os 

basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    """
    Set my configuration variables 
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SERCRET_KEY')