# -*- encoding=utf-8 -*-

from app.models import db


class Movie(db.Model):
    movie_name = db.Column(db.String(40), unique=True, nullable=False, primary_key=True)
    chinese_name = db.Column(db.String(120), unique=True, nullable=False)
    score = db.Column(db.Float, nullable=True)
    director = db.Column(db.String(160), nullable=False)
    actor = db.Column(db.String(160), nullable=False)
    cat_eyes_normal_price = db.Column(db.Float, nullable=True)
    cat_eyes_member_price = db.Column(db.Float, nullable=True)
    tao_bao_normal_price = db.Column(db.Float, nullable=True)
    tao_bao_member_price = db.Column(db.Float, nullable=True)
    comments = db.relationship('Comment', backref='comments', lazy='dynamic')

    def __init__(self, movie_name, chinese_name, director, actor):
        self.movie_name = movie_name
        self.chinese_name = chinese_name
        self.director = director
        self.actor = actor

    def __repr__(self):
        return '<MovieName:%r, ChineseName:%r>' % (self.movie_name, self.chinese_name)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 加movie外键的作用是在数据库写入时，不用add所有项目，只需add主项目就可以
    movie = db.relationship('Movie', backref='movie')
    movie_name = db.Column(db.String(40), db.ForeignKey('movie.movie_name'), nullable=False)
    score = db.Column(db.Float, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, movie, score, content):
        self.movie = movie
        self.score = score
        self.content = content

    def __repr__(self):
        return '<MovieName:%r, Score:%f, Content:%r>' % (self.movie_name, self.score, self.content)

