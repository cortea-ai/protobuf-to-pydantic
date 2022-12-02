import time
from typing import Any

from example.example_proto_python_code.example_proto.p2p_validate.demo_pb2 import (
    AnyTest,
    BoolTest,
    BytesTest,
    DoubleTest,
    DurationTest,
    EnumTest,
    Fixed32Test,
    Fixed64Test,
    FloatTest,
    Int32Test,
    Int64Test,
    MapTest,
    MessageIgnoredTest,
    MessageTest,
    NestedMessage,
    OneOfNotTest,
    OneOfTest,
    RepeatedTest,
    Sfixed32Test,
    Sfixed64Test,
    Sint64Test,
    StringTest,
    TimestampTest,
    Uint32Test,
    Uint64Test,
)
from example.p2p_validate_example.gen_code import CustomerField, confloat, conint, customer_any
from protobuf_to_pydantic import msg_to_pydantic_model, pydantic_model_to_py_code


def exp_time() -> float:
    return time.time()


class TestP2pValidate:
    @staticmethod
    def _model_output(msg: Any) -> str:
        local_dict: dict = {
            "CustomerField": CustomerField,
            "confloat": confloat,
            "conint": conint,
            "customer_any": customer_any,
        }
        return pydantic_model_to_py_code(msg_to_pydantic_model(msg, local_dict=local_dict))

    def test_any(self) -> None:
        assert """
class AnyTest(BaseModel):

    class Config:
        arbitrary_types_allowed = True

    required_test: Any = FieldInfo()
    not_in_test: Any = FieldInfo(
        default_factory=Any,
        extra={
            "any_not_in": [
                "type.googleapis.com/google.protobuf.Duration",
                "type.googleapis.com/google.protobuf.Timestamp"
            ]
        })
    in_test: Any = FieldInfo(
        default_factory=Any,
        extra={
            "any_in": [
                "type.googleapis.com/google.protobuf.Timestamp",
                Any(type_url='type.googleapis.com/google.protobuf.Duration')
            ]
        })
    default_test: Any = FieldInfo(default=Any(
        type_url='type.googleapis.com/google.protobuf.Duration'))
    default_factory_test: Any = FieldInfo(default_factory=customer_any)
    miss_default_test: Any = FieldInfo()
    alias_test: Any = FieldInfo(default_factory=Any,
                                alias="alias",
                                alias_priority=2)
    desc_test: Any = FieldInfo(default_factory=Any, description="test desc")
    example_test: Any = FieldInfo(
        default_factory=Any,
        extra={"example": "type.googleapis.com/google.protobuf.Duration"})
    example_factory_test: Any = FieldInfo(default_factory=Any,
                                          extra={"example": customer_any})
    field_test: Any = CustomerField(default_factory=Any)
    title_test: Any = FieldInfo(default_factory=Any, title="title_test")

    any_not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(any_not_in_validator)
    any_in_validator_in_test = validator('in_test',
                                         allow_reuse=True)(any_in_validator)""" in self._model_output(AnyTest)

    def test_bool(self) -> None:
        assert """
class BoolTest(BaseModel):
    bool_1_test: bool = FieldInfo(default=True, const=True)
    bool_2_test: bool = FieldInfo(default=False, const=True)
    default_test: bool = FieldInfo(default=True)
    miss_default_test: bool = FieldInfo()
    alias_test: bool = FieldInfo(default=False,
                                 alias="alias",
                                 alias_priority=2)
    desc_test: bool = FieldInfo(default=False, description="test desc")
    example_test: bool = FieldInfo(default=False, extra={"example": True})
    field_test: bool = CustomerField(default=False)
    title_test: bool = FieldInfo(default=False, title="title_test")""" in self._model_output(BoolTest)

    def test_bytes(self) -> None:
        assert """
class BytesTest(BaseModel):
    const_test: bytes = FieldInfo(default=b"demo", const=True)
    range_len_test: bytes = FieldInfo(default=b"", min_length=1, max_length=4)
    prefix_test: bytes = FieldInfo(default=b"", extra={"prefix": b"prefix"})
    suffix_test: bytes = FieldInfo(default=b"", extra={"suffix": b"suffix"})
    contains_test: bytes = FieldInfo(default=b"",
                                     extra={"contains": b"contains"})
    in_test: bytes = FieldInfo(default=b"", extra={"in": [b"a", b"b", b"c"]})
    not_in_test: bytes = FieldInfo(default=b"",
                                   extra={"not_in": [b"a", b"b", b"c"]})
    default_test: bytes = FieldInfo(default=b"default")
    default_factory_test: bytes = FieldInfo(default_factory=bytes)
    miss_default_test: bytes = FieldInfo()
    alias_test: bytes = FieldInfo(default=b"", alias="alias", alias_priority=2)
    desc_test: bytes = FieldInfo(default=b"", description="test desc")
    example_test: bytes = FieldInfo(default=b"", extra={"example": b"example"})
    example_factory_test: bytes = FieldInfo(default=b"",
                                            extra={"example": bytes})
    field_test: bytes = CustomerField(default=b"")
    title_test: bytes = FieldInfo(default=b"", title="title_test")
    type_test: constr() = FieldInfo(default=b"")

    prefix_validator_prefix_test = validator(
        'prefix_test', allow_reuse=True)(prefix_validator)
    suffix_validator_suffix_test = validator(
        'suffix_test', allow_reuse=True)(suffix_validator)
    contains_validator_contains_test = validator(
        'contains_test', allow_reuse=True)(contains_validator)
    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(BytesTest)

    def test_double(self) -> None:
        assert """
class DoubleTest(BaseModel):
    const_test: float = FieldInfo(default=1.0, const=True)
    range_e_test: float = FieldInfo(default=0.0, ge=1, le=10)
    range_test: float = FieldInfo(default=0.0, gt=1, lt=10)
    in_test: float = FieldInfo(default=0.0, extra={"in": [1.0, 2.0, 3.0]})
    not_in_test: float = FieldInfo(default=0.0,
                                   extra={"not_in": [1.0, 2.0, 3.0]})
    default_test: float = FieldInfo(default=1.0)
    default_factory_test: float = FieldInfo(default_factory=float)
    miss_default_test: float = FieldInfo()
    alias_test: float = FieldInfo(default=0.0, alias="alias", alias_priority=2)
    desc_test: float = FieldInfo(default=0.0, description="test desc")
    multiple_of_test: float = FieldInfo(default=0.0, multiple_of=3)
    example_test: float = FieldInfo(default=0.0, extra={"example": 1.0})
    example_factory: float = FieldInfo(default=0.0, extra={"example": float})
    field_test: float = CustomerField(default=0.0)
    type_test: confloat() = FieldInfo(default=0.0)
    title_test: float = FieldInfo(default=0.0, title="title_test")

    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(DoubleTest)

    def test_duration(self) -> None:
        assert """
class DurationTest(BaseModel):
    const_test: Timedelta = FieldInfo(
        default_factory=Timedelta,
        extra={"duration_const": timedelta(seconds=1, microseconds=500000)})
    range_test: Timedelta = FieldInfo(default_factory=Timedelta,
                                      extra={
                                          "duration_gt":
                                          timedelta(seconds=5,
                                                    microseconds=500000),
                                          "duration_lt":
                                          timedelta(seconds=10,
                                                    microseconds=500000)
                                      })
    range_e_test: Timedelta = FieldInfo(default_factory=Timedelta,
                                        extra={
                                            "duration_ge":
                                            timedelta(seconds=5,
                                                      microseconds=500000),
                                            "duration_le":
                                            timedelta(seconds=10,
                                                      microseconds=500000)
                                        })
    in_test: Timedelta = FieldInfo(default_factory=Timedelta,
                                   extra={
                                       "duration_in": [
                                           timedelta(seconds=1,
                                                     microseconds=500000),
                                           timedelta(seconds=3,
                                                     microseconds=500000)
                                       ]
                                   })
    not_in_test: Timedelta = FieldInfo(default_factory=Timedelta,
                                       extra={
                                           "duration_not_in": [
                                               timedelta(seconds=1,
                                                         microseconds=500000),
                                               timedelta(seconds=3,
                                                         microseconds=500000)
                                           ]
                                       })
    default_test: Timedelta = FieldInfo(
        default=timedelta(seconds=1, microseconds=500000))
    default_factory_test: Timedelta = FieldInfo(default_factory=timedelta)
    miss_default_test: Timedelta = FieldInfo()
    alias_test: Timedelta = FieldInfo(default_factory=Timedelta,
                                      alias="alias",
                                      alias_priority=2)
    desc_test: Timedelta = FieldInfo(default_factory=Timedelta,
                                     description="test desc")
    example_test: Timedelta = FieldInfo(
        default_factory=Timedelta,
        extra={"example": timedelta(seconds=1, microseconds=500000)})
    example_factory_test: Timedelta = FieldInfo(default_factory=Timedelta,
                                                extra={"example": timedelta})
    field_test: Timedelta = CustomerField(default_factory=Timedelta)
    title_test: Timedelta = FieldInfo(default_factory=Timedelta,
                                      title="title_test")
    type_test: timedelta = FieldInfo(default_factory=Timedelta)

    duration_const_validator_const_test = validator(
        'const_test', allow_reuse=True)(duration_const_validator)
    duration_lt_validator_range_test = validator(
        'range_test', allow_reuse=True)(duration_lt_validator)
    duration_gt_validator_range_test = validator(
        'range_test', allow_reuse=True)(duration_gt_validator)
    duration_le_validator_range_e_test = validator(
        'range_e_test', allow_reuse=True)(duration_le_validator)
    duration_ge_validator_range_e_test = validator(
        'range_e_test', allow_reuse=True)(duration_ge_validator)
    duration_in_validator_in_test = validator(
        'in_test', allow_reuse=True)(duration_in_validator)
    duration_not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(duration_not_in_validator)""" in self._model_output(DurationTest)

    def test_enum(self) -> None:
        assert """
class State(IntEnum):
    INACTIVE = 0
    PENDING = 1
    ACTIVE = 2


class EnumTest(BaseModel):
    const_test: State = FieldInfo(default=2, const=True)
    in_test: State = FieldInfo(default=0, extra={"in": [0, 2]})
    not_in_test: State = FieldInfo(default=0, extra={"not_in": [0, 2]})
    default_test: State = FieldInfo(default=1)
    miss_default_test: State = FieldInfo()
    alias_test: State = FieldInfo(default=0, alias="alias", alias_priority=2)
    desc_test: State = FieldInfo(default=0, description="test desc")
    example_test: State = FieldInfo(default=0, extra={"example": 2})
    field_test: State = CustomerField(default=0)
    title_test: State = FieldInfo(default=0, title="title_test")

    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(EnumTest)

    def test_fixed32(self) -> None:
        assert """
class Fixed32Test(BaseModel):
    const_test: float = FieldInfo(default=1, const=True)
    range_e_test: float = FieldInfo(default=0, ge=1, le=10)
    range_test: float = FieldInfo(default=0, gt=1, lt=10)
    in_test: float = FieldInfo(default=0, extra={"in": [1, 2, 3]})
    not_in_test: float = FieldInfo(default=0, extra={"not_in": [1, 2, 3]})
    default_test: float = FieldInfo(default=1.0)
    default_factory_test: float = FieldInfo(default_factory=float)
    miss_default_test: float = FieldInfo()
    alias_test: float = FieldInfo(default=0, alias="alias", alias_priority=2)
    desc_test: float = FieldInfo(default=0, description="test desc")
    multiple_of_test: float = FieldInfo(default=0, multiple_of=3)
    example_test: float = FieldInfo(default=0, extra={"example": 1.0})
    example_factory: float = FieldInfo(default=0, extra={"example": float})
    field_test: float = CustomerField(default=0)
    type_test: confloat() = FieldInfo(default=0)
    title_test: float = FieldInfo(default=0, title="title_test")

    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(Fixed32Test)

    def test_fixed64(self) -> None:
        assert """class Fixed64Test(BaseModel):
    const_test: float = FieldInfo(default=0)
    range_e_test: float = FieldInfo(default=0, ge=1, le=10)
    range_test: float = FieldInfo(default=0, gt=1, lt=10)
    in_test: float = FieldInfo(default=0, extra={"in": [1, 2, 3]})
    not_in_test: float = FieldInfo(default=0, extra={"not_in": [1, 2, 3]})
    default_test: float = FieldInfo(default=1.0)
    default_factory_test: float = FieldInfo(default_factory=float)
    miss_default_test: float = FieldInfo()
    alias_test: float = FieldInfo(default=0, alias="alias", alias_priority=2)
    desc_test: float = FieldInfo(default=0, description="test desc")
    multiple_of_test: float = FieldInfo(default=0, multiple_of=3)
    example_test: float = FieldInfo(default=0, extra={"example": 1.0})
    example_factory: float = FieldInfo(default=0, extra={"example": float})
    field_test: float = CustomerField(default=0)
    type_test: confloat() = FieldInfo(default=0)
    title_test: float = FieldInfo(default=0, title="title_test")

    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(Fixed64Test)

    def test_float(self) -> None:
        assert """class FloatTest(BaseModel):
    const_test: float = FieldInfo(default=1.0, const=True)
    range_e_test: float = FieldInfo(default=0.0, ge=1, le=10)
    range_test: float = FieldInfo(default=0.0, gt=1, lt=10)
    in_test: float = FieldInfo(default=0.0, extra={"in": [1.0, 2.0, 3.0]})
    not_in_test: float = FieldInfo(default=0.0,
                                   extra={"not_in": [1.0, 2.0, 3.0]})
    default_test: float = FieldInfo(default=1.0)
    default_factory_test: float = FieldInfo(default_factory=float)
    miss_default_test: float = FieldInfo()
    alias_test: float = FieldInfo(default=0.0, alias="alias", alias_priority=2)
    desc_test: float = FieldInfo(default=0.0, description="test desc")
    multiple_of_test: float = FieldInfo(default=0.0, multiple_of=3)
    example_test: float = FieldInfo(default=0.0, extra={"example": 1.0})
    example_factory: float = FieldInfo(default=0.0, extra={"example": float})
    field_test: float = CustomerField(default=0.0)
    type_test: confloat() = FieldInfo(default=0.0)
    title_test: float = FieldInfo(default=0.0, title="title_test")

    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(FloatTest)

    def test_int32(self) -> None:
        assert """class Int32Test(BaseModel):
    const_test: int = FieldInfo(default=1, const=True)
    range_e_test: int = FieldInfo(default=0, ge=1, le=10)
    range_test: int = FieldInfo(default=0, gt=1, lt=10)
    in_test: int = FieldInfo(default=0, extra={"in": [1, 2, 3]})
    not_in_test: int = FieldInfo(default=0, extra={"not_in": [1, 2, 3]})
    default_test: int = FieldInfo(default=1.0)
    default_factory_test: int = FieldInfo(default_factory=int)
    miss_default_test: int = FieldInfo()
    alias_test: int = FieldInfo(default=0, alias="alias", alias_priority=2)
    desc_test: int = FieldInfo(default=0, description="test desc")
    multiple_of_test: int = FieldInfo(default=0, multiple_of=3)
    example_test: int = FieldInfo(default=0, extra={"example": 1.0})
    example_factory: int = FieldInfo(default=0, extra={"example": int})
    field_test: int = CustomerField(default=0)
    type_test: confloat() = FieldInfo(default=0)
    title_test: int = FieldInfo(default=0, title="title_test")

    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(Int32Test)

    def test_int64(self) -> None:
        assert """
class Int64Test(BaseModel):
    const_test: int = FieldInfo(default=1, const=True)
    range_e_test: int = FieldInfo(default=0, ge=1, le=10)
    range_test: int = FieldInfo(default=0, gt=1, lt=10)
    in_test: int = FieldInfo(default=0, extra={"in": [1, 2, 3]})
    not_in_test: int = FieldInfo(default=0, extra={"not_in": [1, 2, 3]})
    default_test: int = FieldInfo(default=1.0)
    default_factory_test: int = FieldInfo(default_factory=int)
    miss_default_test: int = FieldInfo()
    alias_test: int = FieldInfo(default=0, alias="alias", alias_priority=2)
    desc_test: int = FieldInfo(default=0, description="test desc")
    multiple_of_test: int = FieldInfo(default=0, multiple_of=3)
    example_test: int = FieldInfo(default=0, extra={"example": 1.0})
    example_factory: int = FieldInfo(default=0, extra={"example": int})
    field_test: int = CustomerField(default=0)
    type_test: confloat() = FieldInfo(default=0)
    title_test: int = FieldInfo(default=0, title="title_test")

    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(Int64Test)

    def test_map(self) -> None:
        assert """
class MapTest(BaseModel):
    pair_test: typing.Dict[str, int] = FieldInfo(default_factory=dict,
                                                 extra={
                                                     "map_max_pairs": 5,
                                                     "map_min_pairs": 1
                                                 })
    keys_test: typing.Dict[constr(min_length=1, max_length=5),
                           int] = FieldInfo(default_factory=dict)
    values_test: typing.Dict[str, conint(ge=5, le=5)] = FieldInfo(
        default_factory=dict)
    keys_values_test: typing.Dict[constr(min_length=1, max_length=5),
                                  contimestamp(
                                      timestamp_gt_now=True)] = FieldInfo(
                                          default_factory=dict)
    default_factory_test: typing.Dict[str,
                                      int] = FieldInfo(default_factory=dict)
    miss_default_test: typing.Dict[str, int] = FieldInfo()
    alias_test: typing.Dict[str, int] = FieldInfo(default_factory=dict,
                                                  alias="alias",
                                                  alias_priority=2)
    desc_test: typing.Dict[str, int] = FieldInfo(default_factory=dict,
                                                 description="test desc")
    example_factory_test: typing.Dict[str,
                                      int] = FieldInfo(default_factory=dict,
                                                       extra={"example": dict})
    field_test: typing.Dict[str, int] = CustomerField(default_factory=dict)
    title_test: typing.Dict[str, int] = FieldInfo(default_factory=dict,
                                                  title="title_test")
    type_test: dict = FieldInfo(default_factory=dict)

    map_min_pairs_validator_pair_test = validator(
        'pair_test', allow_reuse=True)(map_min_pairs_validator)
    map_max_pairs_validator_pair_test = validator(
        'pair_test', allow_reuse=True)(map_max_pairs_validator)""" in self._model_output(MapTest)

    def test_message_ignored(self) -> None:
        assert """
class MessageIgnoredTest(BaseModel):
    const_test: int = FieldInfo(default=0)
    range_e_test: int = FieldInfo(default=0)
    range_test: int = FieldInfo(default=0)""" in self._model_output(MessageIgnoredTest)

    def test_message(self) -> None:
        assert """
class MessageTest(BaseModel):
    skip_test: str = FieldInfo(default="")
    required_test: str = FieldInfo()""" in self._model_output(MessageTest)

    def test_nested(self) -> None:
        assert """
class StringTest(BaseModel):
    const_test: str = FieldInfo(default="aaa", const=True)
    len_test: str = FieldInfo(default="", extra={"len": 3})
    s_range_len_test: str = FieldInfo(default="", min_length=1, max_length=3)
    pattern_test: str = FieldInfo(default="", regex="^test")
    prefix_test: str = FieldInfo(default="", extra={"prefix": "prefix"})
    suffix_test: str = FieldInfo(default="", extra={"suffix": "suffix"})
    contains_test: str = FieldInfo(default="", extra={"contains": "contains"})
    not_contains_test: str = FieldInfo(default="",
                                       extra={"not_contains": "not_contains"})
    in_test: str = FieldInfo(default="", extra={"in": ["a", "b", "c"]})
    not_in_test: str = FieldInfo(default="", extra={"not_in": ["a", "b", "c"]})
    email_test: EmailStr = FieldInfo(default="")
    hostname_test: HostNameStr = FieldInfo(default="")
    ip_test: IPvAnyAddress = FieldInfo(default="")
    ipv4_test: IPv4Address = FieldInfo(default="")
    ipv6_test: IPv6Address = FieldInfo(default="")
    uri_test: AnyUrl = FieldInfo(default="")
    uri_ref_test: UriRefStr = FieldInfo(default="")
    address_test: IPvAnyAddress = FieldInfo(default="")
    uuid_test: UUID = FieldInfo(default="")
    pydantic_type_test: str = FieldInfo(default="")
    default_test: str = FieldInfo(default="default")
    default_factory_test: str = FieldInfo(default_factory=uuid4)
    miss_default_test: str = FieldInfo()
    alias_test: str = FieldInfo(default="", alias="alias", alias_priority=2)
    desc_test: str = FieldInfo(default="", description="test desc")
    example_test: str = FieldInfo(default="", extra={"example": "example"})
    example_factory_test: str = FieldInfo(default="", extra={"example": uuid4})
    field_test: str = CustomerField(default="")
    title_test: str = FieldInfo(default="", title="title_test")
    type_test: constr() = FieldInfo(default="")

    len_validator_len_test = validator('len_test',
                                       allow_reuse=True)(len_validator)
    prefix_validator_prefix_test = validator(
        'prefix_test', allow_reuse=True)(prefix_validator)
    suffix_validator_suffix_test = validator(
        'suffix_test', allow_reuse=True)(suffix_validator)
    contains_validator_contains_test = validator(
        'contains_test', allow_reuse=True)(contains_validator)
    not_contains_validator_not_contains_test = validator(
        'not_contains_test', allow_reuse=True)(not_contains_validator)
    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)


class MapTest(BaseModel):
    pair_test: typing.Dict[str, int] = FieldInfo(default_factory=dict,
                                                 extra={
                                                     "map_max_pairs": 5,
                                                     "map_min_pairs": 1
                                                 })
    keys_test: typing.Dict[constr(min_length=1, max_length=5),
                           int] = FieldInfo(default_factory=dict)
    values_test: typing.Dict[str, conint(ge=5, le=5)] = FieldInfo(
        default_factory=dict)
    keys_values_test: typing.Dict[constr(min_length=1, max_length=5),
                                  contimestamp(
                                      timestamp_gt_now=True)] = FieldInfo(
                                          default_factory=dict)
    default_factory_test: typing.Dict[str,
                                      int] = FieldInfo(default_factory=dict)
    miss_default_test: typing.Dict[str, int] = FieldInfo()
    alias_test: typing.Dict[str, int] = FieldInfo(default_factory=dict,
                                                  alias="alias",
                                                  alias_priority=2)
    desc_test: typing.Dict[str, int] = FieldInfo(default_factory=dict,
                                                 description="test desc")
    example_factory_test: typing.Dict[str,
                                      int] = FieldInfo(default_factory=dict,
                                                       extra={"example": dict})
    field_test: typing.Dict[str, int] = CustomerField(default_factory=dict)
    title_test: typing.Dict[str, int] = FieldInfo(default_factory=dict,
                                                  title="title_test")
    type_test: dict = FieldInfo(default_factory=dict)

    map_min_pairs_validator_pair_test = validator(
        'pair_test', allow_reuse=True)(map_min_pairs_validator)
    map_max_pairs_validator_pair_test = validator(
        'pair_test', allow_reuse=True)(map_max_pairs_validator)


class NestedMessageUserPayMessage(BaseModel):
    bank_number: str = FieldInfo(default="", min_length=13, max_length=19)
    exp: datetime = FieldInfo(default_factory=datetime.now,
                              extra={"timestamp_gt_now": True})
    uuid: UUID = FieldInfo(default="")

    timestamp_gt_now_validator_exp = validator(
        'exp', allow_reuse=True)(timestamp_gt_now_validator)


class NestedMessageNotEnableUserPayMessage(BaseModel):
    bank_number: str = FieldInfo(default="")
    exp: datetime = FieldInfo(default_factory=datetime.now)
    uuid: str = FieldInfo(default="")


class NestedMessage(BaseModel):
    string_in_map_test: typing.Dict[str, StringTest] = FieldInfo(
        default_factory=dict)
    map_in_map_test: typing.Dict[str,
                                 MapTest] = FieldInfo(default_factory=dict)
    user_pay: NestedMessageUserPayMessage = FieldInfo()
    not_enable_user_pay: NestedMessageNotEnableUserPayMessage = FieldInfo()
    empty: None = FieldInfo()""" in self._model_output(NestedMessage)

    def test_one_of_not(self) -> None:
        assert """
class OneOfNotTest(BaseModel):
    _one_of_dict = {
        "p2p_validate_test.OneOfNotTest.id": {
            "fields": {"x", "y"},
            "required": False
        }
    }

    header: str = FieldInfo(default="")
    x: str = FieldInfo(default="")
    y: int = FieldInfo(default=0)

    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)""" in self._model_output(OneOfNotTest)

    def test_one_of(self) -> None:
        assert """
class OneOfTest(BaseModel):
    _one_of_dict = {
        "p2p_validate_test.OneOfTest.id": {
            "fields": {"x", "y"},
            "required": True
        }
    }

    header: str = FieldInfo(default="")
    x: str = FieldInfo(default="")
    y: int = FieldInfo(default=0)

    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)""" in self._model_output(OneOfTest)

    def test_repeated(self) -> None:
        assert """
class RepeatedTest(BaseModel):
    range_test: typing.List[str] = FieldInfo(default_factory=list,
                                             min_items=1,
                                             max_items=5)
    unique_test: typing.List[str] = FieldInfo(default_factory=list,
                                              unique_items=True)
    items_string_test: conlist(item_type=constr(min_length=1, max_length=5),
                               min_items=1,
                               max_items=5) = FieldInfo(default_factory=list)
    items_double_test: conlist(item_type=confloat(gt=1, lt=5),
                               min_items=1,
                               max_items=5) = FieldInfo(default_factory=list)
    items_int32_test: conlist(item_type=conint(gt=1, lt=5),
                              min_items=1,
                              max_items=5) = FieldInfo(default_factory=list)
    items_timestamp_test: conlist(
        item_type=contimestamp(timestamp_gt=1600000000.0,
                               timestamp_lt=1600000010.0),
        min_items=1,
        max_items=5) = FieldInfo(default_factory=list)
    items_duration_test: conlist(item_type=contimedelta(
        duration_ge=timedelta(seconds=10), duration_le=timedelta(seconds=10)),
                                 min_items=1,
                                 max_items=5) = FieldInfo(default_factory=list)
    items_bytes_test: conlist(item_type=conbytes(min_length=1, max_length=5),
                              min_items=1,
                              max_items=5) = FieldInfo(default_factory=list)
    default_factory_test: typing.List[str] = FieldInfo(default_factory=list)
    miss_default_test: typing.List[str] = FieldInfo()
    alias_test: typing.List[str] = FieldInfo(default_factory=list,
                                             alias="alias",
                                             alias_priority=2)
    desc_test: typing.List[str] = FieldInfo(default_factory=list,
                                            description="test desc")
    example_factory_test: typing.List[str] = FieldInfo(default_factory=list,
                                                       extra={"example": list})
    field_test: typing.List[str] = CustomerField(default_factory=list)
    title_test: typing.List[str] = FieldInfo(default_factory=list,
                                             title="title_test")
    type_test: list = FieldInfo(default_factory=list)""" in self._model_output(RepeatedTest)

    def test_sfixed32(self) -> None:
        assert """
class Sfixed32Test(BaseModel):
    const_test: float = FieldInfo(default=0)
    range_e_test: float = FieldInfo(default=0, ge=1, le=10)
    range_test: float = FieldInfo(default=0, gt=1, lt=10)
    in_test: float = FieldInfo(default=0, extra={"in": [1, 2, 3]})
    not_in_test: float = FieldInfo(default=0, extra={"not_in": [1, 2, 3]})
    default_test: float = FieldInfo(default=1.0)
    default_factory_test: float = FieldInfo(default_factory=float)
    miss_default_test: float = FieldInfo()
    alias_test: float = FieldInfo(default=0, alias="alias", alias_priority=2)
    desc_test: float = FieldInfo(default=0, description="test desc")
    multiple_of_test: float = FieldInfo(default=0, multiple_of=3)
    example_test: float = FieldInfo(default=0, extra={"example": 1.0})
    example_factory: float = FieldInfo(default=0, extra={"example": float})
    field_test: float = CustomerField(default=0)
    type_test: confloat() = FieldInfo(default=0)
    title_test: float = FieldInfo(default=0, title="title_test")

    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(Sfixed32Test)

    def test_sfixed64(self) -> None:
        assert """
class Sfixed64Test(BaseModel):
    const_test: float = FieldInfo(default=0)
    range_e_test: float = FieldInfo(default=0, ge=1, le=10)
    range_test: float = FieldInfo(default=0, gt=1, lt=10)
    in_test: float = FieldInfo(default=0, extra={"in": [1, 2, 3]})
    not_in_test: float = FieldInfo(default=0, extra={"not_in": [1, 2, 3]})
    default_test: float = FieldInfo(default=1.0)
    default_factory_test: float = FieldInfo(default_factory=float)
    miss_default_test: float = FieldInfo()
    alias_test: float = FieldInfo(default=0, alias="alias", alias_priority=2)
    desc_test: float = FieldInfo(default=0, description="test desc")
    multiple_of_test: float = FieldInfo(default=0, multiple_of=3)
    example_test: float = FieldInfo(default=0, extra={"example": 1.0})
    example_factory: float = FieldInfo(default=0, extra={"example": float})
    field_test: float = CustomerField(default=0)
    type_test: confloat() = FieldInfo(default=0)
    title_test: float = FieldInfo(default=0, title="title_test")

    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(Sfixed64Test)

    def test_sint64(self) -> None:
        assert """
class Sint64Test(BaseModel):
    const_test: int = FieldInfo(default=1, const=True)
    range_e_test: int = FieldInfo(default=0, ge=1, le=10)
    range_test: int = FieldInfo(default=0, gt=1, lt=10)
    in_test: int = FieldInfo(default=0, extra={"in": [1, 2, 3]})
    not_in_test: int = FieldInfo(default=0, extra={"not_in": [1, 2, 3]})
    default_test: int = FieldInfo(default=1.0)
    default_factory_test: int = FieldInfo(default_factory=int)
    miss_default_test: int = FieldInfo()
    alias_test: int = FieldInfo(default=0, alias="alias", alias_priority=2)
    desc_test: int = FieldInfo(default=0, description="test desc")
    multiple_of_test: int = FieldInfo(default=0, multiple_of=3)
    example_test: int = FieldInfo(default=0, extra={"example": 1.0})
    example_factory: int = FieldInfo(default=0, extra={"example": int})
    field_test: int = CustomerField(default=0)
    type_test: conint() = FieldInfo(default=0)
    title_test: int = FieldInfo(default=0, title="title_test")

    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(Sint64Test)

    def test_string(self) -> None:
        assert """
class StringTest(BaseModel):
    const_test: str = FieldInfo(default="aaa", const=True)
    len_test: str = FieldInfo(default="", extra={"len": 3})
    s_range_len_test: str = FieldInfo(default="", min_length=1, max_length=3)
    pattern_test: str = FieldInfo(default="", regex="^test")
    prefix_test: str = FieldInfo(default="", extra={"prefix": "prefix"})
    suffix_test: str = FieldInfo(default="", extra={"suffix": "suffix"})
    contains_test: str = FieldInfo(default="", extra={"contains": "contains"})
    not_contains_test: str = FieldInfo(default="",
                                       extra={"not_contains": "not_contains"})
    in_test: str = FieldInfo(default="", extra={"in": ["a", "b", "c"]})
    not_in_test: str = FieldInfo(default="", extra={"not_in": ["a", "b", "c"]})
    email_test: EmailStr = FieldInfo(default="")
    hostname_test: HostNameStr = FieldInfo(default="")
    ip_test: IPvAnyAddress = FieldInfo(default="")
    ipv4_test: IPv4Address = FieldInfo(default="")
    ipv6_test: IPv6Address = FieldInfo(default="")
    uri_test: AnyUrl = FieldInfo(default="")
    uri_ref_test: UriRefStr = FieldInfo(default="")
    address_test: IPvAnyAddress = FieldInfo(default="")
    uuid_test: UUID = FieldInfo(default="")
    pydantic_type_test: str = FieldInfo(default="")
    default_test: str = FieldInfo(default="default")
    default_factory_test: str = FieldInfo(default_factory=uuid4)
    miss_default_test: str = FieldInfo()
    alias_test: str = FieldInfo(default="", alias="alias", alias_priority=2)
    desc_test: str = FieldInfo(default="", description="test desc")
    example_test: str = FieldInfo(default="", extra={"example": "example"})
    example_factory_test: str = FieldInfo(default="", extra={"example": uuid4})
    field_test: str = CustomerField(default="")
    title_test: str = FieldInfo(default="", title="title_test")
    type_test: constr() = FieldInfo(default="")

    len_validator_len_test = validator('len_test',
                                       allow_reuse=True)(len_validator)
    prefix_validator_prefix_test = validator(
        'prefix_test', allow_reuse=True)(prefix_validator)
    suffix_validator_suffix_test = validator(
        'suffix_test', allow_reuse=True)(suffix_validator)
    contains_validator_contains_test = validator(
        'contains_test', allow_reuse=True)(contains_validator)
    not_contains_validator_not_contains_test = validator(
        'not_contains_test', allow_reuse=True)(not_contains_validator)
    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(StringTest)

    def test_timestamp(self) -> None:
        assert """
class TimestampTest(BaseModel):
    const_test: datetime = FieldInfo(default_factory=datetime.now,
                                     extra={"timestamp_const": 1600000000.0})
    range_test: datetime = FieldInfo(default_factory=datetime.now,
                                     extra={
                                         "timestamp_gt": 1600000000.0,
                                         "timestamp_lt": 1600000010.0
                                     })
    range_e_test: datetime = FieldInfo(default_factory=datetime.now,
                                       extra={
                                           "timestamp_ge": 1600000000.0,
                                           "timestamp_le": 1600000010.0
                                       })
    lt_now_test: datetime = FieldInfo(default_factory=datetime.now,
                                      extra={"timestamp_lt_now": True})
    gt_now_test: datetime = FieldInfo(default_factory=datetime.now,
                                      extra={"timestamp_gt_now": True})
    within_test: datetime = FieldInfo(
        default_factory=datetime.now,
        extra={"timestamp_within": timedelta(seconds=1)})
    within_and_gt_now_test: datetime = FieldInfo(default_factory=datetime.now,
                                                 extra={
                                                     "timestamp_gt_now":
                                                     True,
                                                     "timestamp_within":
                                                     timedelta(seconds=3600)
                                                 })
    default_test: datetime = FieldInfo(default=1.5)
    default_factory_test: datetime = FieldInfo(default_factory=datetime.now)
    miss_default_test: datetime = FieldInfo()
    alias_test: datetime = FieldInfo(default_factory=datetime.now,
                                     alias="alias",
                                     alias_priority=2)
    desc_test: datetime = FieldInfo(default_factory=datetime.now,
                                    description="test desc")
    example_test: datetime = FieldInfo(default_factory=datetime.now,
                                       extra={"example": 1.5})
    example_factory_test: datetime = FieldInfo(default_factory=datetime.now,
                                               extra={"example": datetime.now})
    field_test: datetime = CustomerField(default_factory=datetime.now)
    title_test: datetime = FieldInfo(default_factory=datetime.now,
                                     title="title_test")
    type_test: datetime = FieldInfo(default_factory=datetime.now)

    timestamp_const_validator_const_test = validator(
        'const_test', allow_reuse=True)(timestamp_const_validator)
    timestamp_lt_validator_range_test = validator(
        'range_test', allow_reuse=True)(timestamp_lt_validator)
    timestamp_gt_validator_range_test = validator(
        'range_test', allow_reuse=True)(timestamp_gt_validator)
    timestamp_le_validator_range_e_test = validator(
        'range_e_test', allow_reuse=True)(timestamp_le_validator)
    timestamp_ge_validator_range_e_test = validator(
        'range_e_test', allow_reuse=True)(timestamp_ge_validator)
    timestamp_lt_now_validator_lt_now_test = validator(
        'lt_now_test', allow_reuse=True)(timestamp_lt_now_validator)
    timestamp_gt_now_validator_gt_now_test = validator(
        'gt_now_test', allow_reuse=True)(timestamp_gt_now_validator)
    timestamp_within_validator_within_test = validator(
        'within_test', allow_reuse=True)(timestamp_within_validator)
    timestamp_gt_now_validator_within_and_gt_now_test = validator(
        'within_and_gt_now_test', allow_reuse=True)(timestamp_gt_now_validator)
    timestamp_within_validator_within_and_gt_now_test = validator(
        'within_and_gt_now_test', allow_reuse=True)(timestamp_within_validator)""" in self._model_output(TimestampTest)

    def test_unit32(self) -> None:
        assert """class Uint32Test(BaseModel):
    const_test: int = FieldInfo(default=1, const=True)
    range_e_test: int = FieldInfo(default=0, ge=1, le=10)
    range_test: int = FieldInfo(default=0, gt=1, lt=10)
    in_test: int = FieldInfo(default=0, extra={"in": [1, 2, 3]})
    not_in_test: int = FieldInfo(default=0, extra={"not_in": [1, 2, 3]})
    default_test: int = FieldInfo(default=1.0)
    default_factory_test: int = FieldInfo(default_factory=int)
    miss_default_test: int = FieldInfo()
    alias_test: int = FieldInfo(default=0, alias="alias", alias_priority=2)
    desc_test: int = FieldInfo(default=0, description="test desc")
    multiple_of_test: int = FieldInfo(default=0, multiple_of=3)
    example_test: int = FieldInfo(default=0, extra={"example": 1.0})
    example_factory: int = FieldInfo(default=0, extra={"example": int})
    field_test: int = CustomerField(default=0)
    type_test: conint() = FieldInfo(default=0)
    title_test: int = FieldInfo(default=0, title="title_test")

    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(Uint32Test)

    def test_unit64(self) -> None:
        assert """
class Uint64Test(BaseModel):
    const_test: int = FieldInfo(default=1, const=True)
    range_e_test: int = FieldInfo(default=0, ge=1, le=10)
    range_test: int = FieldInfo(default=0, gt=1, lt=10)
    in_test: int = FieldInfo(default=0, extra={"in": [1, 2, 3]})
    not_in_test: int = FieldInfo(default=0, extra={"not_in": [1, 2, 3]})
    default_test: int = FieldInfo(default=1.0)
    default_factory_test: int = FieldInfo(default_factory=int)
    miss_default_test: int = FieldInfo()
    alias_test: int = FieldInfo(default=0, alias="alias", alias_priority=2)
    desc_test: int = FieldInfo(default=0, description="test desc")
    multiple_of_test: int = FieldInfo(default=0, multiple_of=3)
    example_test: int = FieldInfo(default=0, extra={"example": 1.0})
    example_factory: int = FieldInfo(default=0, extra={"example": int})
    field_test: int = CustomerField(default=0)
    type_test: conint() = FieldInfo(default=0)
    title_test: int = FieldInfo(default=0, title="title_test")

    in_validator_in_test = validator('in_test', allow_reuse=True)(in_validator)
    not_in_validator_not_in_test = validator(
        'not_in_test', allow_reuse=True)(not_in_validator)""" in self._model_output(Uint64Test)
