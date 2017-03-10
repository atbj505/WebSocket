#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.websocket


class Index(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html')


class SocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()

    # @staticmethod
    def open(self):
        self.write_message('Welcome to WebSocket')


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', Index),
        ('/soc', SocketHandler),
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
