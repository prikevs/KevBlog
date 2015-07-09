#coding:utf8

DEBUG = True

try:
    import sae
    DBNAME = sae.const.MYSQL_DB
    USER = sae.const.MYSQL_USER
    PASSWD = sae.const.MYSQL_PASS
    HOST = sae.const.MYSQL_HOST
    PORT = sae.const.MYSQL_PORT
    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s:%s/%s" %(USER, PASSWD, HOST, PORT, DBNAME)
except:
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"

TOKEN = "123456"

AUTHOR = "Kevince"
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

