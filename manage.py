# -*- encoding=utf-8 -*-

from app.models import db
from app.models import User


db.drop_all()
db.create_all()
admin = User(movieName='123', chineseName='123123123')
db.session.add(admin)
db.session.commit()
print(User.query.all())