# -*- encoding=utf-8 -*-

from app.models import db


class Movie(db.Model):
    movie_name = db.Column(db.String(40), unique=True, nullable=False, primary_key=True)
    chinese_name = db.Column(db.String(120), unique=True, nullable=False)

    # def __init__(self, movie_name, chinese_name):
    #     self.movieName = movie_name
    #     self.chinese_name = chinese_name

    def __repr__(self):
        return '<MovieName:%r, ChineseName:%r>' % (self.movie_name, self.chinese_name)


class Douban(db.Model):
    movie = db.relationship('Movie', backref=db.backref('posts', lazy='dynamic'))
    movie_name = db.Column(db.String(40), db.ForeignKey('movie.movie_name'), primary_key=True)
    director = db.Column(db.String(160), nullable=False)
    actor = db.Column(db.String(160), nullable=False)

    # def __init__(self, movie, movie_name, director, actor):
    #     self.movie = movie
    #     self.movie_name = movie_name
    #     self.director = director
    #     self.actor = actor

    def __repr__(self):
        return '<MovieName:%r, Director:%r, Actor:%r>' % (self.movieName, self.director, self.actor)

