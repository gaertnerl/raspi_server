from flask import Blueprint, request, jsonify
from ..database import User

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/show_all', methods=['GET'])
def get_users():

    users = []
    users_found = User.query.all()

    for user in users_found:
        user_data = {}
        user_data['username'] = user.username,
        user_data['password'] = user.pw_hash,
        users.append(user_data)

    return jsonify({'users': users})
