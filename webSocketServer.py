#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop


class Index(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body>Hello, world!')


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', Index),
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
