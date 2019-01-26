# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/backend.proto

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
  name='google/api/backend.proto',
  package='google.api',
  syntax='proto3',
  serialized_pb=_b('\n\x18google/api/backend.proto\x12\ngoogle.api\"1\n\x07\x42\x61\x63kend\x12&\n\x05rules\x18\x01 \x03(\x0b\x32\x17.google.api.BackendRule\"B\n\x0b\x42\x61\x63kendRule\x12\x10\n\x08selector\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65\x61\x64line\x18\x03 \x01(\x01\x42 \n\x0e\x63om.google.apiB\x0c\x42\x61\x63kendProtoP\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BACKEND = _descriptor.Descriptor(
  name='Backend',
  full_name='google.api.Backend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rules', full_name='google.api.Backend.rules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=89,
)


_BACKENDRULE = _descriptor.Descriptor(
  name='BackendRule',
  full_name='google.api.BackendRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='selector', full_name='google.api.BackendRule.selector', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='google.api.BackendRule.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deadline', full_name='google.api.BackendRule.deadline', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=157,
)

_BACKEND.fields_by_name['rules'].message_type = _BACKENDRULE
DESCRIPTOR.message_types_by_name['Backend'] = _BACKEND
DESCRIPTOR.message_types_by_name['BackendRule'] = _BACKENDRULE

Backend = _reflection.GeneratedProtocolMessageType('Backend', (_message.Message,), dict(
  DESCRIPTOR = _BACKEND,
  __module__ = 'google.api.backend_pb2'
  # @@protoc_insertion_point(class_scope:google.api.Backend)
  ))
_sym_db.RegisterMessage(Backend)

BackendRule = _reflection.GeneratedProtocolMessageType('BackendRule', (_message.Message,), dict(
  DESCRIPTOR = _BACKENDRULE,
  __module__ = 'google.api.backend_pb2'
  # @@protoc_insertion_point(class_scope:google.api.BackendRule)
  ))
_sym_db.RegisterMessage(BackendRule)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\016com.google.apiB\014BackendProtoP\001'))
# @@protoc_insertion_point(module_scope)
