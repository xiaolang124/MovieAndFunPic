# -*- encoding=utf-8 -*-

from app.models import db


class Movie(db.Model):
    movie_name = db.Column(db.String(40), unique=True, nullable=False, primary_key=True)
    chinese_name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, movie_name, chinese_name):
        self.movie_name = movie_name
        self.chinese_name = chinese_name

    def __repr__(self):
        return '<MovieName:%r, ChineseName:%r>' % (self.movie_name, self.chinese_name)


class Douban(db.Model):
    movie = db.relationship('Movie', backref=db.backref('douban', lazy='dynamic'))
    movie_name = db.Column(db.String(40), db.ForeignKey('movie.movie_name'), primary_key=True)
    director = db.Column(db.String(160), nullable=False)
    actor = db.Column(db.String(160), nullable=False)

    def __init__(self, movie, director, actor):
        self.movie = movie
        self.director = director
        self.actor = actor

    def __repr__(self):
        return '<MovieName:%r, Director:%r, Actor:%r>' % (self.movie_name, self.director, self.actor)


class Comment(db.Model):
    douban = db.relationship('Douban', backref=db.backref('comment', lazy='dynamic'))
    movie_name = db.Column(db.String(40), db.ForeignKey('douban.movie_name'), primary_key=True)
    score = db.Column(db.Float, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, douban, score, content):
        self.douban = douban
        self.score = score
        self.content = content

    def __repr__(self):
        return '<MovieName:%r, Score:%f, Content:%r>' % (self.movie_name, self.score, self.content)

