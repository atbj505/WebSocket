#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.websocket
from protobuf import chatMessageFactory


class Index(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html')


class SocketHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, application, request, **kwargs):
        super(SocketHandler, self).__init__(application, request, **kwargs)
        self.clients = set()
        self.chatMessage = chatMessageFactory.ChatMessageFactory()

    # @staticmethod
    def send_to_all(self, message):
        for client in self.clients:
            client.write_message(self.chatMessage.protoBufSerialize(message))

    def on_message(self, message):
        receivedMessage = self.chatMessage.protoBufParse(message)
        self.send_to_all(receivedMessage)

    def open(self):
        data = {
            'message_type': 0,
            'user_id': 1,
            'message_content': 'Welcome to WebSocket',
        }
        self.write_message(self.chatMessage.protoBufSerialize(data))
        self.send_to_all({
            'message_type': 0,
            'user_id': 1,
            'message_content': str(id(self)) + ' has joined',
        })
        self.clients.add(self)

    def on_close(self):
        self.clients.remove(self)
        self.send_to_all({
            'message_type': 0,
            'user_id': 1,
            'message_content': str(id(self)) + ' has left',
        })


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', Index),
        ('/soc', SocketHandler),
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
