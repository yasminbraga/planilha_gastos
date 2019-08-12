from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__, static_url_path='',static_folder='static')
app.config.from_pyfile('config.py')


db = SQLAlchemy(app)
migrate = Migrate(app,db)

toolbar = DebugToolbarExtension(app)

from app.controllers import dashboard, categorias, saidas, entradas, users, home
