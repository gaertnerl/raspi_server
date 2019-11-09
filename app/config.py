"""
This module contains a selection of
configs. The app factory can create
a new app with one of the configs.
"""
import os


config_path = os.path.dirname(__file__)

# default configuration settings
DEFAULT_SECRET_KEY = 'secret'
DEFAULT_SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(config_path, 'database.db'))


class Config:

    SECRET_KEY = DEFAULT_SECRET_KEY
    SQLALCHEMY_DATABASE_URI = DEFAULT_SQLALCHEMY_DATABASE_URI


class DevConfig(Config):

    DEBUG = True


def get_config(config_name):

    if config_name == 'development': return DevConfig()

