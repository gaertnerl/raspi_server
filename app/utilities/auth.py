from jwt import ExpiredSignatureError, InvalidTokenError, decode
from flask import current_app, jsonify


def decode_auth_token(token):
    """
    Decodes the auth token.

    :param token: Encoded jwt token, generated from login route.
    :return: if correct:    List[True, username of token holder]
             if incorrect:  List[False]
    """
    try:
        payload = decode(token, current_app.config.get('SECRET_KEY'))
        return [True, payload['user']]
    except ExpiredSignatureError:
        return [False]
    except InvalidTokenError:
        return [False]


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