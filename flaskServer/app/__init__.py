__author__ = 'Kevans05'

from flask import Flask
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
#from flask.ext.openid import OpenID
from config import basedir


app = Flask(__name__)
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views

