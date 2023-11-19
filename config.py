from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from secrets import token_hex
from os import path


app = Flask(__name__)
app.config['SECRET_KEY'] = str(token_hex(512))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(path.abspath(path.dirname(__file__)), 'data.sql')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)
Migrate(app=app, db=db)

from core import main
from api import apiview

app.register_blueprint(main)
app.register_blueprint(apiview)
