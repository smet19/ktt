from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(80))
    ugroup = db.Column(db.String(10))
    uphone = db.Column(db.String(20))
    umail = db.Column(db.String(255))

class Statistic(db.Model):
    try_id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer, db.ForeignKey(User.id))
    test_id = db.Column(db.Integer)
    passtime = db.Column(db.DateTime)
    result = db.Column(db.String(16))
