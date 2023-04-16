# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example/example_proto/demo/demo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n%example/example_proto/demo/demo.proto\x12\x04user\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a)example/example_proto/common/single.proto"\xc3\x01\n\x0bUserMessage\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x02\x12\x1a\n\x03sex\x18\x04 \x01(\x0e\x32\r.user.SexType\x12\x1e\n\x04\x64\x65mo\x18\x06 \x01(\x0e\x32\x10.single.DemoEnum\x12\x10\n\x08is_adult\x18\x07 \x01(\x08\x12\x11\n\tuser_name\x18\x08 \x01(\t\x12)\n\x0c\x64\x65mo_message\x18\t \x01(\x0b\x32\x13.single.DemoMessage"\xe4\x01\n\nMapMessage\x12/\n\x08user_map\x18\x01 \x03(\x0b\x32\x1d.user.MapMessage.UserMapEntry\x12\x31\n\tuser_flag\x18\x02 \x03(\x0b\x32\x1e.user.MapMessage.UserFlagEntry\x1a\x41\n\x0cUserMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.user.UserMessage:\x02\x38\x01\x1a/\n\rUserFlagEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01"[\n\x0fRepeatedMessage\x12\x10\n\x08str_list\x18\x01 \x03(\t\x12\x10\n\x08int_list\x18\x02 \x03(\x05\x12$\n\tuser_list\x18\x03 \x03(\x0b\x32\x11.user.UserMessage"\x99\x05\n\rNestedMessage\x12;\n\ruser_list_map\x18\x01 \x03(\x0b\x32$.user.NestedMessage.UserListMapEntry\x12\x32\n\x08user_map\x18\x02 \x03(\x0b\x32 .user.NestedMessage.UserMapEntry\x12\x34\n\x08user_pay\x18\x03 \x01(\x0b\x32".user.NestedMessage.UserPayMessage\x12\x35\n\x0cinclude_enum\x18\x04 \x01(\x0e\x32\x1f.user.NestedMessage.IncludeEnum\x12?\n\x13not_enable_user_pay\x18\x05 \x01(\x0b\x32".user.NestedMessage.UserPayMessage\x12%\n\x05\x65mpty\x18\x06 \x01(\x0b\x32\x16.google.protobuf.Empty\x12,\n\x0b\x61\x66ter_refer\x18\x07 \x01(\x0b\x32\x17.user.AfterReferMessage\x1a\\\n\x0eUserPayMessage\x12\x13\n\x0b\x62\x61nk_number\x18\x01 \x01(\t\x12\'\n\x03\x65xp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x1aI\n\x10UserListMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.user.RepeatedMessage:\x02\x38\x01\x1a@\n\x0cUserMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.user.MapMessage:\x02\x38\x01")\n\x0bIncludeEnum\x12\x08\n\x04zero\x10\x00\x12\x07\n\x03one\x10\x01\x12\x07\n\x03two\x10\x02"-\n\x11\x41\x66terReferMessage\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05"_\n\x0bInvoiceItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12 \n\x05items\x18\x04 \x03(\x0b\x32\x11.user.InvoiceItem"\x0e\n\x0c\x45mptyMessage*\x1d\n\x07SexType\x12\x07\n\x03man\x10\x00\x12\t\n\x05women\x10\x01\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "example.example_proto.demo.demo_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MAPMESSAGE_USERMAPENTRY._options = None
    _MAPMESSAGE_USERMAPENTRY._serialized_options = b"8\001"
    _MAPMESSAGE_USERFLAGENTRY._options = None
    _MAPMESSAGE_USERFLAGENTRY._serialized_options = b"8\001"
    _NESTEDMESSAGE_USERLISTMAPENTRY._options = None
    _NESTEDMESSAGE_USERLISTMAPENTRY._serialized_options = b"8\001"
    _NESTEDMESSAGE_USERMAPENTRY._options = None
    _NESTEDMESSAGE_USERMAPENTRY._serialized_options = b"8\001"
    _SEXTYPE._serialized_start = 1502
    _SEXTYPE._serialized_end = 1531
    _USERMESSAGE._serialized_start = 153
    _USERMESSAGE._serialized_end = 348
    _MAPMESSAGE._serialized_start = 351
    _MAPMESSAGE._serialized_end = 579
    _MAPMESSAGE_USERMAPENTRY._serialized_start = 465
    _MAPMESSAGE_USERMAPENTRY._serialized_end = 530
    _MAPMESSAGE_USERFLAGENTRY._serialized_start = 532
    _MAPMESSAGE_USERFLAGENTRY._serialized_end = 579
    _REPEATEDMESSAGE._serialized_start = 581
    _REPEATEDMESSAGE._serialized_end = 672
    _NESTEDMESSAGE._serialized_start = 675
    _NESTEDMESSAGE._serialized_end = 1340
    _NESTEDMESSAGE_USERPAYMESSAGE._serialized_start = 1064
    _NESTEDMESSAGE_USERPAYMESSAGE._serialized_end = 1156
    _NESTEDMESSAGE_USERLISTMAPENTRY._serialized_start = 1158
    _NESTEDMESSAGE_USERLISTMAPENTRY._serialized_end = 1231
    _NESTEDMESSAGE_USERMAPENTRY._serialized_start = 1233
    _NESTEDMESSAGE_USERMAPENTRY._serialized_end = 1297
    _NESTEDMESSAGE_INCLUDEENUM._serialized_start = 1299
    _NESTEDMESSAGE_INCLUDEENUM._serialized_end = 1340
    _AFTERREFERMESSAGE._serialized_start = 1342
    _AFTERREFERMESSAGE._serialized_end = 1387
    _INVOICEITEM._serialized_start = 1389
    _INVOICEITEM._serialized_end = 1484
    _EMPTYMESSAGE._serialized_start = 1486
    _EMPTYMESSAGE._serialized_end = 1500
# @@protoc_insertion_point(module_scope)
