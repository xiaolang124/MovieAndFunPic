# -*- encoding=utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    movieName = db.Column(db.String(80), unique=True, nullable=False,primary_key=True)
    chineseName = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<MovieName:%r,ChineseName:%r>' % self.movieName,self.chineseName