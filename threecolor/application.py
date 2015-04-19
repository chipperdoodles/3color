import os

from flask import Flask
from .tools import misc
from .configs import config

# set application root path
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

instfolder = config.instfolder
THEME_DIR = config.THEME_DIR


def create_site():
    """App factory to create website"""
    if os.path.exists(instfolder):

        app = Flask('threecolor', instance_path=instfolder, instance_relative_config=True)

        # configure flask app from default settings, then overide with settings.cfg
        app.config.from_object('threecolor.configs.default_settings')
        app.config.from_pyfile('settings.cfg')

        # configure paths and folders according to instance path
        app.config['FLATPAGES_ROOT'] = os.path.join(app.instance_path, 'content')
        app.config['IMAGE_DIR'] = os.path.join(app.instance_path, 'images')
        app.config['FREEZER_DESTINATION'] = os.path.join(app.instance_path, app.config['BUILD_DIR'])

        from .site.coolviews import site, pages, freezer
        app.register_blueprint(site)
        pages.init_app(app)
        freezer.init_app(app)

        return app

    else:
        # app = Flask('threecolor')
        #
        # # configure flask app from default settings, then overide with settings.cfg
        # app.config.from_object('threecolor.configs.default_settings')

        misc.make_home(APP_ROOT)

        return app


def create_admin():
    """Place holder for eventual admin site interface"""
    pass
