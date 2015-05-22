
from flask import abort, current_app, Blueprint, render_template, send_from_directory

admin = Blueprint('site', __name__,
                 url_prefix='admin',
                 )

@admin.route('/')
def index():
    return render_template('index.html')
