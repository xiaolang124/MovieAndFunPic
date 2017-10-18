# -*- encoding=utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('test_env.conf')
db = SQLAlchemy(app)

from app.models.model import Movie
from app.models.model import Douban
from app.models.model import Comment
