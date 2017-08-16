# -*- coding: utf-8 -*-
"""
App runner
"""
# System imports
# Third-party imports
import falcon

# Local imports
from history.sample.models import *


# Create resources
device_history = DeviceHistory()


# Create falcon app
app = falcon.API(middleware=[AuthMiddleware()])
app.add_route('/device/{device_id}/history', device_history)


# Useful for debugging problems in API, it works with pdb
if __name__ == '__main__':
    from wsgiref import simple_server  # NOQA
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()