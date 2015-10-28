import os
import shutil

from flask import config
from . import default_settings, default_sites

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Flask instance folder, currently folder named 3color-Press in user's home folder
instfolder = os.path.join(os.path.expanduser("~"), '3color-Press')

sitefolder = os.path.join(instfolder, 'sites')

sitecfg = os.path.join(instfolder, 'sites.cfg')


# configure active working site
site_cfg = config.Config(instfolder)

site_cfg.from_object(default_sites)

if os.path.exists(sitecfg):
    site_cfg.from_pyfile('sites.cfg')

# site dependent configurations
active_sitefolder = os.path.join(sitefolder, site_cfg['ACTIVE_SITE'])

examplecfg = os.path.join(active_sitefolder, 'example.settings.cfg')

THEME_DIR = os.path.join(active_sitefolder, 'themes')

# helper function checks to see if settings.cfg exists or example file is present
def cfg_check(file):
    if os.path.exists(file):
        return True
    elif os.path.exists(examplecfg):
        shutil.copyfile(examplecfg, file)
        return True
    else:
        return False


def make_usr_cfg():
    if os.path.exists(active_sitefolder):

        cfgfile = os.path.join(active_sitefolder, 'settings.cfg')
        cfgcheck = cfg_check(cfgfile)

        # config using subclass of flask Config
        usr_cfg = config.Config(active_sitefolder)
        usr_cfg.from_object(default_settings)

        if cfgcheck is True:
            usr_cfg.from_pyfile(cfgfile)

        # set some path based values
        usr_cfg['FLATPAGES_ROOT'] = os.path.join(active_sitefolder, 'content')
        usr_cfg['FREEZER_DESTINATION'] = os.path.join(active_sitefolder, usr_cfg['BUILD_DIR'])
        usr_cfg['IMAGE_DIR'] = os.path.join(active_sitefolder, 'images')

        # check to see if there is a theme folder with same name as active theme config
        if usr_cfg['ACTIVE_THEME'] is not 'default':

            if os.path.exists(os.path.join(THEME_DIR, usr_cfg['ACTIVE_THEME'])):
                themefolder = os.path.join(THEME_DIR, usr_cfg['ACTIVE_THEME'])
                usr_cfg.from_pyfile(theme_settings.cfg)
                usr_cfg['TEMPLATES'] = os.path.join(themefolder, 'templates')
                usr_cfg['STATIC'] = os.path.join(themefolder, 'static')
            else:
                print('no theme folder')
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
