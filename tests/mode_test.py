# -*- encoding=utf-8 -*-

import os
from app.models import app, db
from app.models import Movie, Comment
import unittest


class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///../unittest.db'
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_empty_db(self):
        test_movie = Movie(movie_name='what', chinese_name='hello',
                           director='oho', actor='yo')
        test_Comment_1 = Comment(score='3.7', content='what', movie=test_movie)
        test_Comment_2 = Comment(score='3.8', content='ha', movie=test_movie)

        db.session.add(test_movie)
        db.session.commit()

        movie = Movie.query.all()[0]
        comments = movie.comments.all()
        assert 'what' in movie.movie_name
        assert 'hello' in movie.chinese_name
        assert 'oho' in movie.director
        assert 3.7 == comments[0].score
        assert 'what' in comments[0].content
        assert 'what' in comments[0].movie_name


if __name__ == '__main__':
    unittest.main()