from flask import Blueprint, request, jsonify
from ..database import User
from ..utilities.auth import check_token

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/promote', methods=['POST'])
@check_token
def promote_user(user):
    """
    Promotes the user specified in username field of
    http header to admin. The requesting user holding
    the token has to be admin.

    :param user: User Object returned from check_token decorator.
    :return: Json{ message: String }, StatusCode:Int
    """
    if user.admin:
        if request.headers['username']:
            username = request.headers['username']
            user = User.query.filter_by(username=username).first()
            user.admin = True
            return jsonify({'message': 'user promoted'}), 200
        else:
            return jsonify({'message': 'username not found'}), 404

    else:
        return jsonify({'message': 'admin status required'}), 403


@bp.route('/get_names', methods=['GET'])
@check_token
def get_users(user):
    """
    Returns a list of all users in a json object.
    The requesting user holding the token has to be admin.

    :param user: User Object returned from check_token decorator.
    :return: Json{ users: List[users]}, StatusCode:Int
    """

    if user.admin:
        names = []
        users_found = User.query.all()

        for user in users_found:
            names.append(user.username)

        return jsonify({'usersnames': names}), 200

    else:
        return jsonify({'message': 'admin status required'}), 403
