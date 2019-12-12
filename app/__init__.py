from flask import Flask
from .database import db, User
from .blueprints import auth, users, development
from werkzeug.security import generate_password_hash


def create_app(dev_mode=True):
    """
    Create an app with the given configuration.

    :param dev_mode:bool, if true, dev config will be used
    :return: Flask Object, the server application.
    """

    app = Flask(__name__)

    if dev_mode:
        app.config.from_pyfile('./configs/dev_config.py')

    # assign app to the database
    # and create all tables.
    db.init_app(app)
    with app.app_context():
        db.create_all() 

    # register blueprints
    app.register_blueprint(auth.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(development.bp)

    return app
