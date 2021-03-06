# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tweets.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tweets.proto',
  package='tweets',
  syntax='proto3',
  serialized_options=b'\n\023ie.ryan.grpc.tweetsB\013TweetsProtoP\001\242\002\002TP',
  serialized_pb=b'\n\x0ctweets.proto\x12\x06tweets\"\"\n\x0fResponseMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x0eRequestMessage\x12\x0f\n\x07message\x18\x01 \x01(\t2S\n\rMessageSender\x12\x42\n\x0bSendMessage\x12\x16.tweets.RequestMessage\x1a\x17.tweets.ResponseMessage\"\x00\x30\x01\x42)\n\x13ie.ryan.grpc.tweetsB\x0bTweetsProtoP\x01\xa2\x02\x02TPb\x06proto3'
)




_RESPONSEMESSAGE = _descriptor.Descriptor(
  name='ResponseMessage',
  full_name='tweets.ResponseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='tweets.ResponseMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=58,
)


_REQUESTMESSAGE = _descriptor.Descriptor(
  name='RequestMessage',
  full_name='tweets.RequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='tweets.RequestMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['ResponseMessage'] = _RESPONSEMESSAGE
DESCRIPTOR.message_types_by_name['RequestMessage'] = _REQUESTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseMessage = _reflection.GeneratedProtocolMessageType('ResponseMessage', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEMESSAGE,
  '__module__' : 'tweets_pb2'
  # @@protoc_insertion_point(class_scope:tweets.ResponseMessage)
  })
_sym_db.RegisterMessage(ResponseMessage)

RequestMessage = _reflection.GeneratedProtocolMessageType('RequestMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTMESSAGE,
  '__module__' : 'tweets_pb2'
  # @@protoc_insertion_point(class_scope:tweets.RequestMessage)
  })
_sym_db.RegisterMessage(RequestMessage)


DESCRIPTOR._options = None

_MESSAGESENDER = _descriptor.ServiceDescriptor(
  name='MessageSender',
  full_name='tweets.MessageSender',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=95,
  serialized_end=178,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='tweets.MessageSender.SendMessage',
    index=0,
    containing_service=None,
    input_type=_REQUESTMESSAGE,
    output_type=_RESPONSEMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MESSAGESENDER)

DESCRIPTOR.services_by_name['MessageSender'] = _MESSAGESENDER

# @@protoc_insertion_point(module_scope)
