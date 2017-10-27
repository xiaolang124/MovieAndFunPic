# -*- encoding=utf-8 -*-

import os
from app.models import app, db
from app.models import Movie, Comment
import unittest


class TestCase(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_empty_db(self):
        test_movie = Movie(movie_name='what', chinese_name='hello',
                           director='oho', actor='yo')
        # test_Comment_1 = Comment(score='3.7', content='what', movie=test_movie)
        # test_Comment_2 = Comment(score='3.8', content='ha', movie=test_movie)

        db.session.add(test_movie)
        db.session.commit()

        movie = Movie.query.all()[0]
        print(movie)
        assert 'what' in movie.movie_name


if __name__ == '__main__':
    unittest.main()