import os
from flask import Flask

#create flas app instance
app = Flask('threecolor', instance_relative_config=True)

#configure flask app from default settings, then overide with settings.cfg
app.config.from_object('threecolor.default_settings')
app.config.from_pyfile('settings.cfg')

# configure paths and folders according to instance path
app.config['FLATPAGES_ROOT'] = os.path.join(app.instance_path, 'content')
app.config['IMAGE_DIR'] = os.path.join(app.instance_path, 'images')
app.config['FREEZER_DESTINATION'] = os.path.join(app.instance_path, app.config['BUILD_DIR'])

from flatpager import pages, freezer
pages.init_app(app)
freezer.init_app(app)

import threecolor.flatpager
import threecolor.publish
