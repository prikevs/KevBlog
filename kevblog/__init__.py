#coding:utf8

from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app
app = create_app()
app.config.from_pyfile('../config.py')

from . import views
