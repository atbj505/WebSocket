#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.websocket
from protobuf import chatMessageFactory


class Index(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html')


class SocketClients(object):
    clients = set()

    @staticmethod
    def getClients():
        return SocketClients.clients

    @staticmethod
    def addClient(socketHandler):
        SocketClients.clients.add(socketHandler)

    @staticmethod
    def removeClient(socketHandler):
        SocketClients.clients.remove(socketHandler)


class SocketHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, application, request, **kwargs):
        super(SocketHandler, self).__init__(application, request, **kwargs)
        self.chatMessage = chatMessageFactory.ChatMessageFactory()

    def send_to_all(self, message):
        for client in SocketClients.getClients():
            client.write_message(self.chatMessage.protoBufSerialize(message))

    def on_message(self, message):
        receivedMessage = self.chatMessage.protoBufParse(message)
        self.send_to_all(message)

    def open(self):
        SocketClients.addClient(self)
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

    def on_close(self):
        SocketClients.removeClient(self)
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
