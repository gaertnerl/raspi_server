from jwt import ExpiredSignatureError, InvalidTokenError, decode
from flask import current_app, request, jsonify
from ..database import User
from functools import wraps


def check_token(f):
    """
    A decorator that handles all token verification logic.
    If the token is valid it returns the user the token was
    assigned to.

    :param f: decorated function
    :return: token valid:   user object from database
             token invalid: json object with an error message
    """
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'auth_token' in request.headers:
            token = request.headers['auth_token']
        else:
            return jsonify({'message': 'token is missing'}), 401
        try:
            payload = decode(token, current_app.config['SECRET_KEY'])
            user = User.query.filter_by(username=payload['user']).first()

        except ExpiredSignatureError:
            return jsonify({'message': 'token expired'}), 401
        except InvalidTokenError:
            return jsonify({'message': 'token invalid'}), 401
        except:
            return jsonify({'message:' 'unknown error occurred'}), 500

        # pass user to decorated function and execute the function
        return f(user, *args, **kwargs)

    return decorator


def password_requirements(password):
    """
    check if given password fulfills requirement.
    :param password: String
    :return: Boolean
    """
    if any(char.isdigit() for char in password):
        if 5 < len(password) < 20:
            return True
    return False


def username_requirements(username):
    """
    check if given username fulfills requirement.
    :param username: String
    :return: Boolean
    """
    if 2 < len(username) < 15:
        return True
    return False