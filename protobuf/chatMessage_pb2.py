# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chatMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chatMessage.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x63hatMessage.proto\"\x86\x01\n\x0b\x43hatMessage\x12+\n\x0cmessage_type\x18\x01 \x01(\x0e\x32\x15.ChatMessage.ChatType\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x17\n\x0fmessage_content\x18\x03 \x01(\t\" \n\x08\x43hatType\x12\n\n\x06SYSTEM\x10\x00\x12\x08\n\x04USER\x10\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CHATMESSAGE_CHATTYPE = _descriptor.EnumDescriptor(
  name='ChatType',
  full_name='ChatMessage.ChatType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SYSTEM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=124,
  serialized_end=156,
)
_sym_db.RegisterEnumDescriptor(_CHATMESSAGE_CHATTYPE)


_CHATMESSAGE = _descriptor.Descriptor(
  name='ChatMessage',
  full_name='ChatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_type', full_name='ChatMessage.message_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ChatMessage.user_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_content', full_name='ChatMessage.message_content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHATMESSAGE_CHATTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=156,
)

_CHATMESSAGE.fields_by_name['message_type'].enum_type = _CHATMESSAGE_CHATTYPE
_CHATMESSAGE_CHATTYPE.containing_type = _CHATMESSAGE
DESCRIPTOR.message_types_by_name['ChatMessage'] = _CHATMESSAGE

ChatMessage = _reflection.GeneratedProtocolMessageType('ChatMessage', (_message.Message,), dict(
  DESCRIPTOR = _CHATMESSAGE,
  __module__ = 'chatMessage_pb2'
  # @@protoc_insertion_point(class_scope:ChatMessage)
  ))
_sym_db.RegisterMessage(ChatMessage)


# @@protoc_insertion_point(module_scope)
