#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from protobuf import chatMessage_pb2


class ChatMessageFactory(object):
    def protoBufSerialize(self, message):
        sendData = None
        if isinstance(message, dict):
            chatMessage = chatMessage_pb2.ChatMessage()
            chatMessage.message_type = message["message_type"]
            chatMessage.user_id = message["user_id"]
            chatMessage.message_content = message["message_content"]
            sendData = chatMessage.SerializeToString()
        elif isinstance(message, chatMessage_pb2.ChatMessage):
            sendDataStr = message.SerializeToString()
        return sendData

    def protoBufParse(self, message):
        receivedMessage = chatMessage_pb2.ChatMessage()
        receivedMessage.ParseFromString(message)
        return receivedMessage
