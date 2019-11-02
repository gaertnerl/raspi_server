from ..__init__ import db


class Users(db.Model):

    __tablename__ = 'users.py'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(60))




