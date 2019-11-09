from flask_sqlalchemy import SQLAlchemy
import re

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    pw_hash = db.Column(db.String(80))
    admin = db.Column(db.Boolean, default=False)
    master_admin = db.Column(db.Boolean, default=False)


class Circuit(db.Model):

    __tablename__ = 'circuit'
    encoding = db.Column(db.Text)


def check_allowed_characters(string):
    if re.match('^[A-Za-z0-9_-]*$', string):
        return True

    return False
