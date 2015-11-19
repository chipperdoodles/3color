import os

from flask import Flask
from .configs import conf

# set application root path
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

instfolder = conf.instfolder
sitefolder = conf.sitefolder
active_sitefolder = conf.active_sitefolder
THEME_DIR = conf.THEME_DIR


def create_site():
    """App factory to create website"""

    if os.path.exists(instfolder):

        app = Flask('threecolor',
                    instance_path=active_sitefolder,
                    instance_relative_config=True
                    )

        # configure app with default config files
        app.config.from_object('threecolor.configs.default_settings')
        app.config.from_object('threecolor.configs.default_template_settings')

        if os.path.exists(os.path.join(active_sitefolder, 'settings.cfg')):
            # overide default settings with user settings
            app.config.from_pyfile('settings.cfg')

        if app.config['ACTIVE_THEME'] is not 'default':
            app.config.from_pyfile(os.path.join(THEME_DIR,
                                   app.config['ACTIVE_THEME'],
                                   'theme_settings.cfg')
                                   )

        # configure paths and folders according to instance path
        app.config['FLATPAGES_ROOT'] = os.path.join(app.instance_path, 'content')
        app.config['IMAGE_DIR'] = os.path.join(app.instance_path, 'images')
        app.config['FREEZER_DESTINATION'] = os.path.join(app.instance_path,
                                                         app.config['BUILD_DIR']
                                                         )

        from .site.coolviews import site, pages, freezer
        app.register_blueprint(site)
        pages.init_app(app)
        freezer.init_app(app)

        return app

    else:
        """a project folder is needed to run"""
        print("no project folder found ")


def create_admin():
    """Place holder for eventual admin site interface"""
    pass
