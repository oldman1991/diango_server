#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/7/18
import json
from urllib.parse import parse_qsl

import falcon

class MethodHandler(object):
    def __init__(self):
        self.post = {}

    def parse_post_data(self, req):
        assert isinstance(req, falcon.Request)
        body = req.stream.read()
        body = body.decode('ascii')
        print(body)
        prams_list = parse_qsl(body, keep_blank_values=True)
        for key, value in prams_list:
            self.post[key] = value
        print(prams_list)
        # print(prams_list)

class V1(MethodHandler):


    def on_post(self, req, resp):
        assert isinstance(req, falcon.Request)
        assert isinstance(resp, falcon.Response)

        self.parse_post_data(req)


        # method = self.post_get_param('method')
        # params_json = self.post_get_param('params')
        #
        #
        # params = json.loads(params_json)

        response = {"code":1}
        response_body = json.dumps(response) + '\n'
        resp.content_type = 'application/json'
        resp.body = response_body


def get_wsgi_app():

    falcon_instance = falcon.API(
        middleware=[]
    )

    falcon_instance.req_options.keep_blank_qs_values = True
    falcon_instance.req_options.auto_parse_form_urlencoded = False

    # falcon_instance.add_route('/ping', Ping())
    # falcon_instance.add_route('/version', ServerVersion())
    # falcon_instance.add_route("/system/statuses", SystemStatuses(dispatcher=dispatcher))
    # falcon_instance.add_route("/schema", SchemaView()),
    falcon_instance.add_route('/v1/once', V1())
    # falcon_instance.add_route('/v1/batch', V1Batch(dispatcher=dispatcher))

    return falcon_instance