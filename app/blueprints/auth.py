"""
Blueprint that contains all views
that handle authentication.
"""

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from jwt import encode
import datetime

from ..database import db, User, check_allowed_characters

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    auth = request.authorization

    # check if the request is valid
    if not auth:
        return jsonify({'message': 'no authorization in header'}), 400
    if not auth.username:
        return jsonify({'message': 'username required'}), 400
    if not auth.password:
        return jsonify({'message': 'password required'}), 400

    # check if characters are allowed
    if not check_allowed_characters(auth.password):
        return jsonify({'message': 'illegal characters in password'}), 400
    if not check_allowed_characters(auth.username):
        return jsonify({'message': 'illegal characters in username'}), 400

    # check if username and password meet requirements
    if not check_password(auth.password):
        return jsonify({'message': 'password does not meet requirements'}), 400
    if not check_username(auth.username):
        return jsonify({'message': 'username does not meet requirements'}), 400

    # check if user already exists in database
    if User.query.filter_by(username=auth.username).first():
        return jsonify({'message': 'user already exists'}), 403

    else:
        pw_hash = generate_password_hash(auth.password, method='sha256')
        user = User(username=auth.username, pw_hash=pw_hash)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'new user registered'}), 200


def check_password(password):
    if any(char.isdigit() for char in password):
        if 5 < len(password) < 20:
            return True
    return False


def check_username(username):
    if 2 < len(username) < 15:
        return True
    return False
