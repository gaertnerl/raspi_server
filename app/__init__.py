from flask import Flask
from .config import get_config
from .database import db
from .blueprints import auth


def create_app(config_name='dev_config'):
    # Create an app with the given
    # configuration.
    #
    # config_name: String, config that should be used

    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    # assign app to the database
    # and create all tables.
    db.init_app(app)
    db.create_all()

    # register blueprints
    app.register_blueprint(auth.bp)

    @app.route('/ping')
    def pong():
        return 'pong', 200

    return app
