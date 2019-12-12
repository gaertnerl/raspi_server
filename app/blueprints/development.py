from flask import Blueprint, jsonify
from werkzeug.security import generate_password_hash

from ..utilities.auth import password_requirements, username_requirements
from ..database import db, User, check_allowed_characters

bp = Blueprint('dev', __name__, url_prefix='/dev')


@bp.route('/create_super_user', methods=['POST'])
def create_super_user():
    """ Create an admin user for development purposes.
    :return: ok message
    """

    super_u = User(
        username='super',
        password=generate_password_hash('super'),
        admin=True,)

    db.session.add(super_u)
    db.session.commit()

    return jsonify({'message': 'super user created'}), 200


@bp.route('/ping', methods=['GET'])
def pong():
    return jsonify({'message': 'pong'}), 200
