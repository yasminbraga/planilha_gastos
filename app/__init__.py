from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__, static_url_path='',static_folder='static')
app.config.from_object(os.getenv('APP_SETTINGS', 'config.Production'))


db = SQLAlchemy(app)
migrate = Migrate(app,db)


from app.controllers import dashboard, categorias, saidas, entradas, users, home
