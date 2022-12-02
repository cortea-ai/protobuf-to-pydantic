# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example_proto/common/validate.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#example_proto/common/validate.proto\x12\x08validate\x1a google/protobuf/descriptor.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x98\x07\n\nFieldRules\x12\'\n\x07message\x18\x11 \x01(\x0b\x32\x16.validate.MessageRules\x12%\n\x05\x66loat\x18\x01 \x01(\x0b\x32\x14.validate.FloatRulesH\x00\x12\'\n\x06\x64ouble\x18\x02 \x01(\x0b\x32\x15.validate.DoubleRulesH\x00\x12%\n\x05int32\x18\x03 \x01(\x0b\x32\x14.validate.Int32RulesH\x00\x12%\n\x05int64\x18\x04 \x01(\x0b\x32\x14.validate.Int64RulesH\x00\x12\'\n\x06uint32\x18\x05 \x01(\x0b\x32\x15.validate.UInt32RulesH\x00\x12\'\n\x06uint64\x18\x06 \x01(\x0b\x32\x15.validate.UInt64RulesH\x00\x12\'\n\x06sint32\x18\x07 \x01(\x0b\x32\x15.validate.SInt32RulesH\x00\x12\'\n\x06sint64\x18\x08 \x01(\x0b\x32\x15.validate.SInt64RulesH\x00\x12)\n\x07\x66ixed32\x18\t \x01(\x0b\x32\x16.validate.Fixed32RulesH\x00\x12)\n\x07\x66ixed64\x18\n \x01(\x0b\x32\x16.validate.Fixed64RulesH\x00\x12+\n\x08sfixed32\x18\x0b \x01(\x0b\x32\x17.validate.SFixed32RulesH\x00\x12+\n\x08sfixed64\x18\x0c \x01(\x0b\x32\x17.validate.SFixed64RulesH\x00\x12#\n\x04\x62ool\x18\r \x01(\x0b\x32\x13.validate.BoolRulesH\x00\x12\'\n\x06string\x18\x0e \x01(\x0b\x32\x15.validate.StringRulesH\x00\x12%\n\x05\x62ytes\x18\x0f \x01(\x0b\x32\x14.validate.BytesRulesH\x00\x12#\n\x04\x65num\x18\x10 \x01(\x0b\x32\x13.validate.EnumRulesH\x00\x12+\n\x08repeated\x18\x12 \x01(\x0b\x32\x17.validate.RepeatedRulesH\x00\x12!\n\x03map\x18\x13 \x01(\x0b\x32\x12.validate.MapRulesH\x00\x12!\n\x03\x61ny\x18\x14 \x01(\x0b\x32\x12.validate.AnyRulesH\x00\x12+\n\x08\x64uration\x18\x15 \x01(\x0b\x32\x17.validate.DurationRulesH\x00\x12-\n\ttimestamp\x18\x16 \x01(\x0b\x32\x18.validate.TimestampRulesH\x00\x42\x06\n\x04type"\x7f\n\nFloatRules\x12\r\n\x05\x63onst\x18\x01 \x01(\x02\x12\n\n\x02lt\x18\x02 \x01(\x02\x12\x0b\n\x03lte\x18\x03 \x01(\x02\x12\n\n\x02gt\x18\x04 \x01(\x02\x12\x0b\n\x03gte\x18\x05 \x01(\x02\x12\n\n\x02in\x18\x06 \x03(\x02\x12\x0e\n\x06not_in\x18\x07 \x03(\x02\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08"\x80\x01\n\x0b\x44oubleRules\x12\r\n\x05\x63onst\x18\x01 \x01(\x01\x12\n\n\x02lt\x18\x02 \x01(\x01\x12\x0b\n\x03lte\x18\x03 \x01(\x01\x12\n\n\x02gt\x18\x04 \x01(\x01\x12\x0b\n\x03gte\x18\x05 \x01(\x01\x12\n\n\x02in\x18\x06 \x03(\x01\x12\x0e\n\x06not_in\x18\x07 \x03(\x01\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08"\x7f\n\nInt32Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x05\x12\n\n\x02lt\x18\x02 \x01(\x05\x12\x0b\n\x03lte\x18\x03 \x01(\x05\x12\n\n\x02gt\x18\x04 \x01(\x05\x12\x0b\n\x03gte\x18\x05 \x01(\x05\x12\n\n\x02in\x18\x06 \x03(\x05\x12\x0e\n\x06not_in\x18\x07 \x03(\x05\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08"\x7f\n\nInt64Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x03\x12\n\n\x02lt\x18\x02 \x01(\x03\x12\x0b\n\x03lte\x18\x03 \x01(\x03\x12\n\n\x02gt\x18\x04 \x01(\x03\x12\x0b\n\x03gte\x18\x05 \x01(\x03\x12\n\n\x02in\x18\x06 \x03(\x03\x12\x0e\n\x06not_in\x18\x07 \x03(\x03\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08"\x80\x01\n\x0bUInt32Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\r\x12\n\n\x02lt\x18\x02 \x01(\r\x12\x0b\n\x03lte\x18\x03 \x01(\r\x12\n\n\x02gt\x18\x04 \x01(\r\x12\x0b\n\x03gte\x18\x05 \x01(\r\x12\n\n\x02in\x18\x06 \x03(\r\x12\x0e\n\x06not_in\x18\x07 \x03(\r\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08"\x80\x01\n\x0bUInt64Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x04\x12\n\n\x02lt\x18\x02 \x01(\x04\x12\x0b\n\x03lte\x18\x03 \x01(\x04\x12\n\n\x02gt\x18\x04 \x01(\x04\x12\x0b\n\x03gte\x18\x05 \x01(\x04\x12\n\n\x02in\x18\x06 \x03(\x04\x12\x0e\n\x06not_in\x18\x07 \x03(\x04\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08"\x80\x01\n\x0bSInt32Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x11\x12\n\n\x02lt\x18\x02 \x01(\x11\x12\x0b\n\x03lte\x18\x03 \x01(\x11\x12\n\n\x02gt\x18\x04 \x01(\x11\x12\x0b\n\x03gte\x18\x05 \x01(\x11\x12\n\n\x02in\x18\x06 \x03(\x11\x12\x0e\n\x06not_in\x18\x07 \x03(\x11\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08"\x80\x01\n\x0bSInt64Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x12\x12\n\n\x02lt\x18\x02 \x01(\x12\x12\x0b\n\x03lte\x18\x03 \x01(\x12\x12\n\n\x02gt\x18\x04 \x01(\x12\x12\x0b\n\x03gte\x18\x05 \x01(\x12\x12\n\n\x02in\x18\x06 \x03(\x12\x12\x0e\n\x06not_in\x18\x07 \x03(\x12\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08"\x81\x01\n\x0c\x46ixed32Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x07\x12\n\n\x02lt\x18\x02 \x01(\x07\x12\x0b\n\x03lte\x18\x03 \x01(\x07\x12\n\n\x02gt\x18\x04 \x01(\x07\x12\x0b\n\x03gte\x18\x05 \x01(\x07\x12\n\n\x02in\x18\x06 \x03(\x07\x12\x0e\n\x06not_in\x18\x07 \x03(\x07\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08"\x81\x01\n\x0c\x46ixed64Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x06\x12\n\n\x02lt\x18\x02 \x01(\x06\x12\x0b\n\x03lte\x18\x03 \x01(\x06\x12\n\n\x02gt\x18\x04 \x01(\x06\x12\x0b\n\x03gte\x18\x05 \x01(\x06\x12\n\n\x02in\x18\x06 \x03(\x06\x12\x0e\n\x06not_in\x18\x07 \x03(\x06\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08"\x82\x01\n\rSFixed32Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x0f\x12\n\n\x02lt\x18\x02 \x01(\x0f\x12\x0b\n\x03lte\x18\x03 \x01(\x0f\x12\n\n\x02gt\x18\x04 \x01(\x0f\x12\x0b\n\x03gte\x18\x05 \x01(\x0f\x12\n\n\x02in\x18\x06 \x03(\x0f\x12\x0e\n\x06not_in\x18\x07 \x03(\x0f\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08"\x82\x01\n\rSFixed64Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x10\x12\n\n\x02lt\x18\x02 \x01(\x10\x12\x0b\n\x03lte\x18\x03 \x01(\x10\x12\n\n\x02gt\x18\x04 \x01(\x10\x12\x0b\n\x03gte\x18\x05 \x01(\x10\x12\n\n\x02in\x18\x06 \x03(\x10\x12\x0e\n\x06not_in\x18\x07 \x03(\x10\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08"\x1a\n\tBoolRules\x12\r\n\x05\x63onst\x18\x01 \x01(\x08"\xfd\x03\n\x0bStringRules\x12\r\n\x05\x63onst\x18\x01 \x01(\t\x12\x0b\n\x03len\x18\x13 \x01(\x04\x12\x0f\n\x07min_len\x18\x02 \x01(\x04\x12\x0f\n\x07max_len\x18\x03 \x01(\x04\x12\x11\n\tlen_bytes\x18\x14 \x01(\x04\x12\x11\n\tmin_bytes\x18\x04 \x01(\x04\x12\x11\n\tmax_bytes\x18\x05 \x01(\x04\x12\x0f\n\x07pattern\x18\x06 \x01(\t\x12\x0e\n\x06prefix\x18\x07 \x01(\t\x12\x0e\n\x06suffix\x18\x08 \x01(\t\x12\x10\n\x08\x63ontains\x18\t \x01(\t\x12\x14\n\x0cnot_contains\x18\x17 \x01(\t\x12\n\n\x02in\x18\n \x03(\t\x12\x0e\n\x06not_in\x18\x0b \x03(\t\x12\x0f\n\x05\x65mail\x18\x0c \x01(\x08H\x00\x12\x12\n\x08hostname\x18\r \x01(\x08H\x00\x12\x0c\n\x02ip\x18\x0e \x01(\x08H\x00\x12\x0e\n\x04ipv4\x18\x0f \x01(\x08H\x00\x12\x0e\n\x04ipv6\x18\x10 \x01(\x08H\x00\x12\r\n\x03uri\x18\x11 \x01(\x08H\x00\x12\x11\n\x07uri_ref\x18\x12 \x01(\x08H\x00\x12\x11\n\x07\x61\x64\x64ress\x18\x15 \x01(\x08H\x00\x12\x0e\n\x04uuid\x18\x16 \x01(\x08H\x00\x12\x30\n\x10well_known_regex\x18\x18 \x01(\x0e\x32\x14.validate.KnownRegexH\x00\x12\x14\n\x06strict\x18\x19 \x01(\x08:\x04true\x12\x14\n\x0cignore_empty\x18\x1a \x01(\x08\x42\x0c\n\nwell_known"\xfb\x01\n\nBytesRules\x12\r\n\x05\x63onst\x18\x01 \x01(\x0c\x12\x0b\n\x03len\x18\r \x01(\x04\x12\x0f\n\x07min_len\x18\x02 \x01(\x04\x12\x0f\n\x07max_len\x18\x03 \x01(\x04\x12\x0f\n\x07pattern\x18\x04 \x01(\t\x12\x0e\n\x06prefix\x18\x05 \x01(\x0c\x12\x0e\n\x06suffix\x18\x06 \x01(\x0c\x12\x10\n\x08\x63ontains\x18\x07 \x01(\x0c\x12\n\n\x02in\x18\x08 \x03(\x0c\x12\x0e\n\x06not_in\x18\t \x03(\x0c\x12\x0c\n\x02ip\x18\n \x01(\x08H\x00\x12\x0e\n\x04ipv4\x18\x0b \x01(\x08H\x00\x12\x0e\n\x04ipv6\x18\x0c \x01(\x08H\x00\x12\x14\n\x0cignore_empty\x18\x0e \x01(\x08\x42\x0c\n\nwell_known"L\n\tEnumRules\x12\r\n\x05\x63onst\x18\x01 \x01(\x05\x12\x14\n\x0c\x64\x65\x66ined_only\x18\x02 \x01(\x08\x12\n\n\x02in\x18\x03 \x03(\x05\x12\x0e\n\x06not_in\x18\x04 \x03(\x05".\n\x0cMessageRules\x12\x0c\n\x04skip\x18\x01 \x01(\x08\x12\x10\n\x08required\x18\x02 \x01(\x08"\x80\x01\n\rRepeatedRules\x12\x11\n\tmin_items\x18\x01 \x01(\x04\x12\x11\n\tmax_items\x18\x02 \x01(\x04\x12\x0e\n\x06unique\x18\x03 \x01(\x08\x12#\n\x05items\x18\x04 \x01(\x0b\x32\x14.validate.FieldRules\x12\x14\n\x0cignore_empty\x18\x05 \x01(\x08"\xa3\x01\n\x08MapRules\x12\x11\n\tmin_pairs\x18\x01 \x01(\x04\x12\x11\n\tmax_pairs\x18\x02 \x01(\x04\x12\x11\n\tno_sparse\x18\x03 \x01(\x08\x12"\n\x04keys\x18\x04 \x01(\x0b\x32\x14.validate.FieldRules\x12$\n\x06values\x18\x05 \x01(\x0b\x32\x14.validate.FieldRules\x12\x14\n\x0cignore_empty\x18\x06 \x01(\x08"8\n\x08\x41nyRules\x12\x10\n\x08required\x18\x01 \x01(\x08\x12\n\n\x02in\x18\x02 \x03(\t\x12\x0e\n\x06not_in\x18\x03 \x03(\t"\xbb\x02\n\rDurationRules\x12\x10\n\x08required\x18\x01 \x01(\x08\x12(\n\x05\x63onst\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12%\n\x02lt\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12&\n\x03lte\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12%\n\x02gt\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12&\n\x03gte\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12%\n\x02in\x18\x07 \x03(\x0b\x32\x19.google.protobuf.Duration\x12)\n\x06not_in\x18\x08 \x03(\x0b\x32\x19.google.protobuf.Duration"\xba\x02\n\x0eTimestampRules\x12\x10\n\x08required\x18\x01 \x01(\x08\x12)\n\x05\x63onst\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02lt\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03lte\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02gt\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03gte\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06lt_now\x18\x07 \x01(\x08\x12\x0e\n\x06gt_now\x18\x08 \x01(\x08\x12)\n\x06within\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration*F\n\nKnownRegex\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x14\n\x10HTTP_HEADER_NAME\x10\x01\x12\x15\n\x11HTTP_HEADER_VALUE\x10\x02:2\n\x08\x64isabled\x12\x1f.google.protobuf.MessageOptions\x18\xaf\x08 \x01(\x08:1\n\x07ignored\x12\x1f.google.protobuf.MessageOptions\x18\xb0\x08 \x01(\x08:0\n\x08required\x12\x1d.google.protobuf.OneofOptions\x18\xaf\x08 \x01(\x08:C\n\x05rules\x12\x1d.google.protobuf.FieldOptions\x18\xaf\x08 \x01(\x0b\x32\x14.validate.FieldRulesBP\n\x1aio.envoyproxy.pgv.validateZ2github.com/envoyproxy/protoc-gen-validate/validate'
)

_KNOWNREGEX = DESCRIPTOR.enum_types_by_name["KnownRegex"]
KnownRegex = enum_type_wrapper.EnumTypeWrapper(_KNOWNREGEX)
UNKNOWN = 0
HTTP_HEADER_NAME = 1
HTTP_HEADER_VALUE = 2

DISABLED_FIELD_NUMBER = 1071
disabled = DESCRIPTOR.extensions_by_name["disabled"]
IGNORED_FIELD_NUMBER = 1072
ignored = DESCRIPTOR.extensions_by_name["ignored"]
REQUIRED_FIELD_NUMBER = 1071
required = DESCRIPTOR.extensions_by_name["required"]
RULES_FIELD_NUMBER = 1071
rules = DESCRIPTOR.extensions_by_name["rules"]

_FIELDRULES = DESCRIPTOR.message_types_by_name["FieldRules"]
_FLOATRULES = DESCRIPTOR.message_types_by_name["FloatRules"]
_DOUBLERULES = DESCRIPTOR.message_types_by_name["DoubleRules"]
_INT32RULES = DESCRIPTOR.message_types_by_name["Int32Rules"]
_INT64RULES = DESCRIPTOR.message_types_by_name["Int64Rules"]
_UINT32RULES = DESCRIPTOR.message_types_by_name["UInt32Rules"]
_UINT64RULES = DESCRIPTOR.message_types_by_name["UInt64Rules"]
_SINT32RULES = DESCRIPTOR.message_types_by_name["SInt32Rules"]
_SINT64RULES = DESCRIPTOR.message_types_by_name["SInt64Rules"]
_FIXED32RULES = DESCRIPTOR.message_types_by_name["Fixed32Rules"]
_FIXED64RULES = DESCRIPTOR.message_types_by_name["Fixed64Rules"]
_SFIXED32RULES = DESCRIPTOR.message_types_by_name["SFixed32Rules"]
_SFIXED64RULES = DESCRIPTOR.message_types_by_name["SFixed64Rules"]
_BOOLRULES = DESCRIPTOR.message_types_by_name["BoolRules"]
_STRINGRULES = DESCRIPTOR.message_types_by_name["StringRules"]
_BYTESRULES = DESCRIPTOR.message_types_by_name["BytesRules"]
_ENUMRULES = DESCRIPTOR.message_types_by_name["EnumRules"]
_MESSAGERULES = DESCRIPTOR.message_types_by_name["MessageRules"]
_REPEATEDRULES = DESCRIPTOR.message_types_by_name["RepeatedRules"]
_MAPRULES = DESCRIPTOR.message_types_by_name["MapRules"]
_ANYRULES = DESCRIPTOR.message_types_by_name["AnyRules"]
_DURATIONRULES = DESCRIPTOR.message_types_by_name["DurationRules"]
_TIMESTAMPRULES = DESCRIPTOR.message_types_by_name["TimestampRules"]
FieldRules = _reflection.GeneratedProtocolMessageType(
    "FieldRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _FIELDRULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.FieldRules)
    },
)
_sym_db.RegisterMessage(FieldRules)

FloatRules = _reflection.GeneratedProtocolMessageType(
    "FloatRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _FLOATRULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.FloatRules)
    },
)
_sym_db.RegisterMessage(FloatRules)

DoubleRules = _reflection.GeneratedProtocolMessageType(
    "DoubleRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _DOUBLERULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.DoubleRules)
    },
)
_sym_db.RegisterMessage(DoubleRules)

Int32Rules = _reflection.GeneratedProtocolMessageType(
    "Int32Rules",
    (_message.Message,),
    {
        "DESCRIPTOR": _INT32RULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.Int32Rules)
    },
)
_sym_db.RegisterMessage(Int32Rules)

Int64Rules = _reflection.GeneratedProtocolMessageType(
    "Int64Rules",
    (_message.Message,),
    {
        "DESCRIPTOR": _INT64RULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.Int64Rules)
    },
)
_sym_db.RegisterMessage(Int64Rules)

UInt32Rules = _reflection.GeneratedProtocolMessageType(
    "UInt32Rules",
    (_message.Message,),
    {
        "DESCRIPTOR": _UINT32RULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.UInt32Rules)
    },
)
_sym_db.RegisterMessage(UInt32Rules)

UInt64Rules = _reflection.GeneratedProtocolMessageType(
    "UInt64Rules",
    (_message.Message,),
    {
        "DESCRIPTOR": _UINT64RULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.UInt64Rules)
    },
)
_sym_db.RegisterMessage(UInt64Rules)

SInt32Rules = _reflection.GeneratedProtocolMessageType(
    "SInt32Rules",
    (_message.Message,),
    {
        "DESCRIPTOR": _SINT32RULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.SInt32Rules)
    },
)
_sym_db.RegisterMessage(SInt32Rules)

SInt64Rules = _reflection.GeneratedProtocolMessageType(
    "SInt64Rules",
    (_message.Message,),
    {
        "DESCRIPTOR": _SINT64RULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.SInt64Rules)
    },
)
_sym_db.RegisterMessage(SInt64Rules)

Fixed32Rules = _reflection.GeneratedProtocolMessageType(
    "Fixed32Rules",
    (_message.Message,),
    {
        "DESCRIPTOR": _FIXED32RULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.Fixed32Rules)
    },
)
_sym_db.RegisterMessage(Fixed32Rules)

Fixed64Rules = _reflection.GeneratedProtocolMessageType(
    "Fixed64Rules",
    (_message.Message,),
    {
        "DESCRIPTOR": _FIXED64RULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.Fixed64Rules)
    },
)
_sym_db.RegisterMessage(Fixed64Rules)

SFixed32Rules = _reflection.GeneratedProtocolMessageType(
    "SFixed32Rules",
    (_message.Message,),
    {
        "DESCRIPTOR": _SFIXED32RULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.SFixed32Rules)
    },
)
_sym_db.RegisterMessage(SFixed32Rules)

SFixed64Rules = _reflection.GeneratedProtocolMessageType(
    "SFixed64Rules",
    (_message.Message,),
    {
        "DESCRIPTOR": _SFIXED64RULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.SFixed64Rules)
    },
)
_sym_db.RegisterMessage(SFixed64Rules)

BoolRules = _reflection.GeneratedProtocolMessageType(
    "BoolRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _BOOLRULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.BoolRules)
    },
)
_sym_db.RegisterMessage(BoolRules)

StringRules = _reflection.GeneratedProtocolMessageType(
    "StringRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _STRINGRULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.StringRules)
    },
)
_sym_db.RegisterMessage(StringRules)

BytesRules = _reflection.GeneratedProtocolMessageType(
    "BytesRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _BYTESRULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.BytesRules)
    },
)
_sym_db.RegisterMessage(BytesRules)

EnumRules = _reflection.GeneratedProtocolMessageType(
    "EnumRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENUMRULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.EnumRules)
    },
)
_sym_db.RegisterMessage(EnumRules)

MessageRules = _reflection.GeneratedProtocolMessageType(
    "MessageRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _MESSAGERULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.MessageRules)
    },
)
_sym_db.RegisterMessage(MessageRules)

RepeatedRules = _reflection.GeneratedProtocolMessageType(
    "RepeatedRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _REPEATEDRULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.RepeatedRules)
    },
)
_sym_db.RegisterMessage(RepeatedRules)

MapRules = _reflection.GeneratedProtocolMessageType(
    "MapRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _MAPRULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.MapRules)
    },
)
_sym_db.RegisterMessage(MapRules)

AnyRules = _reflection.GeneratedProtocolMessageType(
    "AnyRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _ANYRULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.AnyRules)
    },
)
_sym_db.RegisterMessage(AnyRules)

DurationRules = _reflection.GeneratedProtocolMessageType(
    "DurationRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _DURATIONRULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.DurationRules)
    },
)
_sym_db.RegisterMessage(DurationRules)

TimestampRules = _reflection.GeneratedProtocolMessageType(
    "TimestampRules",
    (_message.Message,),
    {
        "DESCRIPTOR": _TIMESTAMPRULES,
        "__module__": "example_proto.common.validate_pb2"
        # @@protoc_insertion_point(class_scope:validate.TimestampRules)
    },
)
_sym_db.RegisterMessage(TimestampRules)

if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(disabled)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(ignored)
    google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(required)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(rules)

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\n\032io.envoyproxy.pgv.validateZ2github.com/envoyproxy/protoc-gen-validate/validate"
    )
    _KNOWNREGEX._serialized_start = 4553
    _KNOWNREGEX._serialized_end = 4623
    _FIELDRULES._serialized_start = 149
    _FIELDRULES._serialized_end = 1069
    _FLOATRULES._serialized_start = 1071
    _FLOATRULES._serialized_end = 1198
    _DOUBLERULES._serialized_start = 1201
    _DOUBLERULES._serialized_end = 1329
    _INT32RULES._serialized_start = 1331
    _INT32RULES._serialized_end = 1458
    _INT64RULES._serialized_start = 1460
    _INT64RULES._serialized_end = 1587
    _UINT32RULES._serialized_start = 1590
    _UINT32RULES._serialized_end = 1718
    _UINT64RULES._serialized_start = 1721
    _UINT64RULES._serialized_end = 1849
    _SINT32RULES._serialized_start = 1852
    _SINT32RULES._serialized_end = 1980
    _SINT64RULES._serialized_start = 1983
    _SINT64RULES._serialized_end = 2111
    _FIXED32RULES._serialized_start = 2114
    _FIXED32RULES._serialized_end = 2243
    _FIXED64RULES._serialized_start = 2246
    _FIXED64RULES._serialized_end = 2375
    _SFIXED32RULES._serialized_start = 2378
    _SFIXED32RULES._serialized_end = 2508
    _SFIXED64RULES._serialized_start = 2511
    _SFIXED64RULES._serialized_end = 2641
    _BOOLRULES._serialized_start = 2643
    _BOOLRULES._serialized_end = 2669
    _STRINGRULES._serialized_start = 2672
    _STRINGRULES._serialized_end = 3181
    _BYTESRULES._serialized_start = 3184
    _BYTESRULES._serialized_end = 3435
    _ENUMRULES._serialized_start = 3437
    _ENUMRULES._serialized_end = 3513
    _MESSAGERULES._serialized_start = 3515
    _MESSAGERULES._serialized_end = 3561
    _REPEATEDRULES._serialized_start = 3564
    _REPEATEDRULES._serialized_end = 3692
    _MAPRULES._serialized_start = 3695
    _MAPRULES._serialized_end = 3858
    _ANYRULES._serialized_start = 3860
    _ANYRULES._serialized_end = 3916
    _DURATIONRULES._serialized_start = 3919
    _DURATIONRULES._serialized_end = 4234
    _TIMESTAMPRULES._serialized_start = 4237
    _TIMESTAMPRULES._serialized_end = 4551
# @@protoc_insertion_point(module_scope)
