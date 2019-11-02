from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
import config

# choose a config
config_name = 'default'


db = SQLAlchemy()

app = Flask(__name__)

config = config.get_config(config_name)

app.config.from_object(config)

db.init_app(app)
