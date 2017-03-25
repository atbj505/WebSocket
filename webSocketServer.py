#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.websocket
from protobuf.chatMessage_pb2 import ChatMessage


class Index(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html')


class SocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()

    @staticmethod
    def send_to_all(message):
        for c in SocketHandler.clients:
            c.write_message(json.dumps(message))

    def on_message(self, message):
        SocketHandler.send_to_all({
            'type': 'user',
            'id': id(self),
            'message': message,
        })

    def protoBufData(self, **data):
        chatMessage = ChatMessage()
        chatMessage.type = data[type]
        chatMessage.id = data[id]
        chatMessage.content = data[content]
        sendDataStr = chatMessage.SerializeToString()
        return sendDataStr

    def open(self):
        self.write_message(json.dumps({
            'type': 'sys',
            'message': 'Welcome to WebSocket',
        }))
        SocketHandler.send_to_all({
            'type': 'sys',
            'message': str(id(self)) + ' has joined',
        })
        SocketHandler.clients.add(self)

    def on_close(self):
        SocketHandler.clients.remove(self)
        SocketHandler.send_to_all({
            'type': 'sys',
            'message': str(id(self)) + ' has left',
        })


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', Index),
        ('/soc', SocketHandler),
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
