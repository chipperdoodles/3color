import os
import shutil

from flask import config
from . import default_settings

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Flask instance folder, currently folder named 3color-Press in user's home folder
instfolder = os.path.join(os.path.expanduser("~"), '3color-Press')

examplecfg = os.path.join(instfolder, 'example.settings.cfg')

THEME_DIR = os.path.join(instfolder, 'themes')


def cfg_check(file):
    if os.path.exists(file):
        return True
    elif os.path.exists(examplecfg):
        shutil.copyfile(examplecfg, file)
        return True
    else:
        return False


def make_usr_cfg():
    if os.path.exists(instfolder):

        cfgfile = os.path.join(instfolder, 'settings.cfg')
        cfgcheck = cfg_check(cfgfile)

        # config using subclass of flask Config
        usr_cfg = config.Config(instfolder)
        usr_cfg.from_object(default_settings)

        if cfgcheck is True:
            usr_cfg.from_pyfile(cfgfile)

        # configure some path based values
        usr_cfg['TEMPLATES'] = os.path.join(THEME_DIR, usr_cfg['ACTIVE_THEME'], 'templates')
        usr_cfg['STATIC'] = os.path.join(THEME_DIR, usr_cfg['ACTIVE_THEME'], 'static')
        usr_cfg['FLATPAGES_ROOT'] = os.path.join(instfolder, 'content')
        usr_cfg['FREEZER_DESTINATION'] = os.path.join(instfolder, usr_cfg['BUILD_DIR'])

        # check to see if there is a theme folder with same name as active theme config
        if os.path.exists(os.path.join(THEME_DIR, usr_cfg['ACTIVE_THEME'])):
            usr_cfg['IMAGE_DIR'] = os.path.join(instfolder, 'images')
        else:
            usr_cfg['TEMPLATES'] = 'templates'
            usr_cfg['STATIC'] = 'static'

        return usr_cfg

    else:
        usr_cfg = config.Config(APP_ROOT)
        usr_cfg.from_object(default_settings)

        usr_cfg['TEMPLATES'] = 'templates'
        usr_cfg['STATIC'] = 'static'

        return usr_cfg
