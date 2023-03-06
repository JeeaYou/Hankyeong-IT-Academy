from pybo import db

class Question(db.Model):  # 테이블을 class 로 만든다
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)   # 글자 제한
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(30), unique=True, nullable=False)

