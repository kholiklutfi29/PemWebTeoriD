from flask import Flask
import os
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
app_folder_path = os.path.abspath("app")
from app.controller import routes
from app.models import gambar
