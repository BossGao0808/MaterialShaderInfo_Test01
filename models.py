from exts import db
from datetime import datetime

class EmailCaptchaModel(db.Model):
    __tablename__='email_captcha'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    captcha = db.Column(db.String(10),nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(200),nullable=False,unique=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(200),nullable=False)
    join_time = db.Column(db.DateTime,default=datetime.now)


class ShaderInfoModel(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Project = db.Column(db.String(200),nullable=False)
    add_time= db.Column(db.DateTime,default=datetime.now())
    filepath= db.Column(db.Text,nullable=False)
    Describe= db.Column(db.Text)

