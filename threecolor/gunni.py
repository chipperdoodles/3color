from __future__ import unicode_literals

import multiprocessing
import gunicorn.app.base

from gunicorn.six import iteritems
from threecolor.application import create_site


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1

options = {
    'bind': '%s:%s' % ('127.0.0.1', '5001'),
    'workers': number_of_workers(),
    }

def test_app(environ, start_response):
    response_body = b'Works fine'
    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
    ]

    start_response(status, response_headers)

    return [response_body]


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


# if __name__ == '__main__':
#     options = {
#         'bind': '%s:%s' % ('127.0.0.1', '8080'),
#         'workers': number_of_workers(),
#     }
#     StandaloneApplication(create_site(), options).run()
