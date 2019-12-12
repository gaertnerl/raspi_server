"""
Blueprint that contains all views
that handle authentication.
"""

from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from jwt import encode
import datetime

from ..utilities.auth import password_requirements, username_requirements
from ..database import db, User, check_allowed_characters

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    """
    Creates a database entry for a new user. Reads the
    new username and password from an auth field in the
    http header. A new user will only be created if given
    username and password meet the syntactical requirements.

    :return: String, an error or an OK message.
    """
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
    if not password_requirements(auth.password):
        return jsonify({'message': 'password does not meet requirements'}), 400
    if not username_requirements(auth.username):
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


@bp.route('/login', methods=['POST'])
def login():
    """
    The apps login route. Will return a token if
    the login was successful. Expect an auth field
    in the http header.

    :return: String, JWT web token with an expiration time
    and the username as payload.
    """
    auth = request.authorization

    user = User.query.filter_by(username=auth.username).first()

    if not user:
        return jsonify({'message': 'username not found'}), 403

    # if password matches database record, return new token
    if check_password_hash(user.pw_hash, auth.password):
        token = encode({
            'user': auth.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
            current_app.config['SECRET_KEY'])

        # return token UTF-8 encoded since it is in bytecode
        return jsonify({'token': token.decode('UTF-8')}), 200
    else:
        return jsonify({'message:': 'Password and username do not match.'}), 401


