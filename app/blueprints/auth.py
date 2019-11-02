"""
Blueprint that contains all views
that handle authentication.
"""

import functools
from flask import Blueprint, request, jsonify

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        auth = request.authorization

        if not auth:
            return jsonify({'message': 'no authorization in header'}), 400

        if not auth.username:
            return jsonify({'message': 'username required'}), 400

        if not auth.password:
            return jsonify({'message': 'password required'}), 400




