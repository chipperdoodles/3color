import os
from flask import Flask

app = Flask('threecolor')
app = Flask(__name__.split('.')[0], instance_relative_config=True)

app.config.from_object('threecolor.default_settings')
app.config.from_pyfile('settings.cfg')
app.config['FLATPAGES_ROOT'] = os.path.join(app.instance_path, 'content')
app.config['IMAGE_DIR'] = os.path.join(app.instance_path, 'images')
app.config['FREEZER_DESTINATION'] = os.path.join(os.getcwd(), app.config['BUILD_DIR'])

from flatpager import pages
pages.init_app(app)

# import threecolor.flatpager
import threecolor.flatpager
