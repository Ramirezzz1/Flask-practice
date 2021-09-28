
from app2 import app2
from flask import render_template

@app2.route('/')
def home():
    return render_template('index.html')


