import os

from flask import Flask

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
instfolder = os.path.join(APP_ROOT, 'instance')

def create_site():
    #create flask app instance
    app = Flask('threecolor',instance_path=instfolder ,instance_relative_config=True)

    #configure flask app from default settings, then overide with settings.cfg
    app.config.from_object('threecolor.configs.default_settings')
    app.config.from_pyfile('settings.cfg')

    # if os.path.exists(app.instance_path):
    #     pass
    # else:
    #     pass

    # configure paths and folders according to instance path
    app.config['FLATPAGES_ROOT'] = os.path.join(app.instance_path, 'content')
    app.config['IMAGE_DIR'] = os.path.join(app.instance_path, 'images')
    app.config['FREEZER_DESTINATION'] = os.path.join(app.instance_path, app.config['BUILD_DIR'])

    from .site.coolviews import site, pages, freezer
    app.register_blueprint(site)
    pages.init_app(app)
    freezer.init_app(app)

    return app

def create_admin():
    pass
