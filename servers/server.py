#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/7/18
from wsgiref.simple_server import make_server

from servers.wsgi_app import get_wsgi_app


def do_server(*, host, port):
    application = get_wsgi_app()
    server = make_server(host,port,app=application)
    try:
        server.serve_forever()
    finally:
        server.server_close()
