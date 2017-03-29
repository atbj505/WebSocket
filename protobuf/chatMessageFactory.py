
from protobuf.chatMessage_pb2 import ChatMessage


class ChatMessageFactory(object):
    def protoBufSerialize(self, message):
        sendData = None
        if isinstance(message, dict):
            chatMessage = ChatMessage()
            chatMessage.message_type = message["message_type"]
            chatMessage.user_id = message["user_id"]
            chatMessage.message_content = message["message_content"]
            sendData = chatMessage.SerializeToString()
        elif isinstance(message, ChatMessage):
            sendDataStr = message.SerializeToString()
        return sendData

    def protoBufParse(self, message):
        receivedMessage = ChatMessage()
        receivedMessage.ParseFromString(message)
        return receivedMessage
