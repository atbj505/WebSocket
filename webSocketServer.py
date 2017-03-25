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
            c.write_message(self.protoBufSerialize(message))

    def on_message(self, message):
        receivedMessage = self.protoBufParse(message)
        SocketHandler.send_to_all(receivedMessage)

    def protoBufSerialize(self, message):
        sendDataStr = None
        if isinstance(message, dict):
            chatMessage = ChatMessage()
            chatMessage.message_type = message["message_type"]
            chatMessage.user_id = message["user_id"]
            chatMessage.message_content = message["message_content"]
            sendDataStr = chatMessage.SerializeToString()
        elif isinstance(message, ChatMessage):
            sendDataStr = message.SerializeToString()
        return sendDataStr

    def protoBufParse(self, str):
        receivedMessage = ChatMessage()
        receivedMessage.ParseFromString(str)
        return receivedMessage

    def open(self):
        data = {
            'message_type': 0,
            'user_id': 1,
            'message_content': 'Welcome to WebSocket',
        }
        self.write_message(self.protoBufSerialize(data))
        SocketHandler.send_to_all({
            'message_type': 0,
            'user_id': 1,
            'message_content': str(id(self)) + ' has joined',
        })
        SocketHandler.clients.add(self)

    def on_close(self):
        SocketHandler.clients.remove(self)
        SocketHandler.send_to_all({
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
