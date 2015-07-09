#coding:utf8

from flask.ext.sqlalchemy import SQLAlchemy
from . import app
'''
import sae
class nullpool_SQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        super(nullpool_SQLAlchemy, self).apply_driver_hacks(app, info, options)
        from sqlalchemy.pool import NullPool
        options['poolclass'] = NullPool
        del options['pool_size']

db = nullpool_SQLAlchemy(app)
'''

db = SQLAlchemy(app)
