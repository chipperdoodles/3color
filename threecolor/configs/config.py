import os

from flask import config
from . import default_settings

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#flask instance folder, currently foldern named 3color Press in user's home folder
instfolder = os.path.join(os.path.expanduser("~"), '3color Press')

# TODO add check for themes folder and make config rules based for that
THEME_DIR = os.path.join(instfolder, 'themes')

def make_usr_cfg():
    if os.path.exists(instfolder):

        cfgfile = os.path.join(instfolder, 'settings.cfg')

        usr_cfg = config.Config(instfolder)
        usr_cfg.from_object(default_settings)
        usr_cfg.from_pyfile(cfgfile)

        usr_cfg['TEMPLATES'] = os.path.join(THEME_DIR, usr_cfg['ACTIVE_THEME'], 'templates')
        usr_cfg['STATIC'] = os.path.join(THEME_DIR, usr_cfg['ACTIVE_THEME'], 'static')
        usr_cfg['FLATPAGES_ROOT'] = os.path.join(instfolder, 'content')

        usr_cfg['IMAGE_DIR'] = os.path.join(instfolder, 'images')
        usr_cfg['FREEZER_DESTINATION'] = os.path.join(instfolder, usr_cfg['BUILD_DIR'])

        return usr_cfg

    else:
        usr_cfg = config.Config(APP_ROOT)
        usr_cfg.from_object(default_settings)

        usr_cfg['TEMPLATES'] = 'templates'
        usr_cfg['STATIC'] = 'static'

        return usr_cfg
