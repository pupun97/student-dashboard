from flask_login import UserMixin

from flask_app import db


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(55))
    f_name = db.Column(db.String(55))
    dob = db.Column(db.Date())
    address = db.Column(db.String(255))
    city = db.Column(db.String(55))
    state = db.Column(db.String(55))
    pin = db.Column(db.Integer)
    phone_no = db.Column(db.String(13), unique=True)
    email = db.Column(db.String(55), unique=True)
    class_opted = db.Column(db.Integer)
    marks = db.Column(db.Integer)

    date_enroll = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    updated_on = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp(), nullable=False)


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique=True)
    password = db.Column(db.String(55), unique=True)
