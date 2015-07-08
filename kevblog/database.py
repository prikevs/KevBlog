#coding:utf8

from sqlalchemy.pool import NullPool
from flask.ext.sqlalchemy import SQLAlchemy
from . import app

db = SQLAlchemy(app)
