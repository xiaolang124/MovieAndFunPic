# -*- encoding=utf-8 -*-

from app.models import db
from app.models import Movie


db.drop_all()
db.create_all()
admin = Movie(movie_name='123', chinese_name='123123123')
db.session.add(admin)
db.session.commit()
print(Movie.query.all())

