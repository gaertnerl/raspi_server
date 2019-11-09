from flask import Blueprint, request, jsonify
from ..database import User
from ..utilities.auth import decode_auth_token

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/show_all', methods=['GET'])
def get_users():
    
    token = request.headers.get('auth_token')

    if not token:
        return jsonify({'message': 'no token provided'}), 401

    token_data = decode_auth_token(token)

    if not token_data[0]:
        return jsonify({'message': 'Token expired or invalid'}), 401

    username = token_data[1]
    user = User.query.filter_by(username=username).first()

    if user.admin:
        users = []
        users_found = User.query.all()

        for user in users_found:
            user_data = {}
            user_data['username'] = user.username,
            user_data['password'] = user.pw_hash,
            users.append(user_data)

        return jsonify({'users': users}), 200

    else:
        return jsonify({'message': 'access denied, user is not admin'}), 403
