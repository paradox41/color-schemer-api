import sys
import logging
import configargparse

from flask import Flask, current_app
from flask.ext.sqlalchemy import SQLAlchemy
from flask_oauthlib.client import OAuth

log = logging.getLogger(__name__)

__version__ = '0.1.0'

db = SQLAlchemy()
oauth = OAuth()


def get_configargparse_config():
    p = configargparse.ArgParser(
        default_config_files=['.color_schemer'])
    # this option can be set in a config file because it starts with '--'
    p.add('--SECRET_KEY', required=False, env_var='SECRET_KEY')
    p.add('--SQLALCHEMY_DATABASE_URI', required=True, env_var='SQLALCHEMY_DATABASE_URI')
    p.add('--LOG_LEVEL', required=False, env_var='LOG_LEVEL', default=logging.INFO)

    options = p.parse_args()

    return options


def setup_logging(app=current_app):
    logging.basicConfig()

    log.setLevel(app.config.get('LOG_LEVEL', logging.DEBUG))

    flask_oauthlib_log = logging.getLogger('flask_oauthlib')
    flask_oauthlib_log.addHandler(logging.StreamHandler(sys.stdout))
    flask_oauthlib_log.setLevel(app.config.get('LOG_LEVEL', logging.DEBUG))

    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


def create_app(config=None):
    log.debug('creating app with config: %s', config)

    import color_schemer.default_config
    from color_schemer.auth import auth_blueprint, login_manager
    from color_schemer.core import color_schemer_api

    app = Flask(__name__, instance_relative_config=True)

    if config:
        app.config.from_object(config)
    else:
        app.config.from_object(color_schemer.default_config)

    app.register_blueprint(auth_blueprint)

    setup_logging(app)

    db.init_app(app)
    oauth.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(color_schemer_api, url_prefix='/api')

    app.db = db

    return app
