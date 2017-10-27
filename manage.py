# -*- encoding=utf-8 -*-

from app.models import db
from app.models import Movie, Comment

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    test_movie = Movie(movie_name='123', chinese_name='123123123',
                       director='oho', actor='yo')
    test_Comment_1 = Comment(score='3.7', content='鬼', movie=test_movie)
    test_Comment_2 = Comment(score='3.8', content='什么', movie=test_movie)

    db.session.add(test_movie)
    db.session.add(test_Comment_1)
    db.session.add(test_Comment_2)
    db.session.commit()

    movie = Movie.query.all()[0]
    comments = movie.comments.all()
    print(comments)
    # for comment in Comment.query.filter_by(movie_name=movie.movie_name).all():
    #     print(comment)
    # query.get()使用的是主键获取

