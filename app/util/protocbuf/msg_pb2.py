# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\tmsg.proto\x12\x0c\x61pp.protobuf\"-\n\x0bSubMessage1\x12\x0e\n\x06\x66ield1\x18\x01 \x01(\x05\x12\x0e\n\x06\x66ield2\x18\x02 \x01(\x05\"-\n\x0bSubMessage2\x12\x0e\n\x06\x66ield1\x18\x01 \x01(\x05\x12\x0e\n\x06\x66ield2\x18\x02 \x01(\t\"m\n\x11MessageBytesExtra\x12+\n\x08message1\x18\x01 \x01(\x0b\x32\x19.app.protobuf.SubMessage1\x12+\n\x08message2\x18\x03 \x03(\x0b\x32\x19.app.protobuf.SubMessage2b\x06proto3')

_SUBMESSAGE1 = DESCRIPTOR.message_types_by_name['SubMessage1']
_SUBMESSAGE2 = DESCRIPTOR.message_types_by_name['SubMessage2']
_MESSAGEBYTESEXTRA = DESCRIPTOR.message_types_by_name['MessageBytesExtra']
SubMessage1 = _reflection.GeneratedProtocolMessageType('SubMessage1', (_message.Message,), {
    'DESCRIPTOR': _SUBMESSAGE1,
    '__module__': 'msg_pb2'
    # @@protoc_insertion_point(class_scope:app.protobuf.SubMessage1)
})
_sym_db.RegisterMessage(SubMessage1)

SubMessage2 = _reflection.GeneratedProtocolMessageType('SubMessage2', (_message.Message,), {
    'DESCRIPTOR': _SUBMESSAGE2,
    '__module__': 'msg_pb2'
    # @@protoc_insertion_point(class_scope:app.protobuf.SubMessage2)
})
_sym_db.RegisterMessage(SubMessage2)

MessageBytesExtra = _reflection.GeneratedProtocolMessageType('MessageBytesExtra', (_message.Message,), {
    'DESCRIPTOR': _MESSAGEBYTESEXTRA,
    '__module__': 'msg_pb2'
    # @@protoc_insertion_point(class_scope:app.protobuf.MessageBytesExtra)
})
_sym_db.RegisterMessage(MessageBytesExtra)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SUBMESSAGE1._serialized_start = 27
    _SUBMESSAGE1._serialized_end = 72
    _SUBMESSAGE2._serialized_start = 74
    _SUBMESSAGE2._serialized_end = 119
    _MESSAGEBYTESEXTRA._serialized_start = 121
    _MESSAGEBYTESEXTRA._serialized_end = 230
# @@protoc_insertion_point(module_scope)
