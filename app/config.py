"""
This module contains a collection
of configs. Flask app can be started
with one of the configs.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# config parameters
DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
DEFAULT_KEY = 'default_key'


class Config:
    """Base class for each config"""

    SECRET_KEY = DEFAULT_KEY
    SQLALCHEMY_DATABASE_URI = DATABASE_URI


class DevConfig(Config):
    """Config for development purposes."""
    DEBUG = True


def get_config(config_name):

    if config_name == 'dev' : return DevConfig
    if config_name == 'default' : return DevConfig


