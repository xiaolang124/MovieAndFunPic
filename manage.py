# -*- encoding=utf-8 -*-

from app.models import db
from app.models import Movie, Douban, Comment


db.drop_all()
db.create_all()
test_movie = Movie(movie_name='123', chinese_name='123123123')
test_douban = Douban(director='hi', actor='hello', movie=test_movie)
test_Comment = Comment(score='3.7', content='what', douban=test_douban)
test_douban.comment.append(test_Comment)
test_movie.douban.append(test_douban)
db.session.add(test_movie)
db.session.commit()

movie = Movie.query.get(0)

# douban = Douban.query.filter_by(movie_name=movie.movie_name)
print(type(movie))
# print(douban)

