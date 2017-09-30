#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#author:WangRui
import os
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import options, define
from tornado.httpclient import HTTPClient
from tornado.httpclient import HTTPRequest
import requests
import uuid


define(name="port", default=9999, type=int)


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/createDes", CreateHandler),
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")



class CreateHandler(tornado.web.RequestHandler):
    def post(self):
        url = self.get_argument("url")
        ico_api_url = "http://www/google.com/s2/favicons?domain=%s" % url
        name = self.get_argument("name")
        response = requests.get(ico_api_url)
        with open(name, 'wb') as f:
            f.write(response.content)


def main():
    tornado.options.parse_command_line()
    print "starting server...."
    print "Starting server on port %d" % options.port
    http_server = Application()
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
