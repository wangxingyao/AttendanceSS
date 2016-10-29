from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
# Above this has a warning, so use the following
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app, use_native_unicode="utf8")

from app import views, models
