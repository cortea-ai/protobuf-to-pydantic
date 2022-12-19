import time
from typing import Any
from uuid import uuid4

from example.example_proto_python_code.example_proto.demo import demo_pb2
from protobuf_to_pydantic import msg_to_pydantic_model, pydantic_model_to_py_code


def exp_time() -> float:
    return time.time()


class BaseTestTextComment:
    @staticmethod
    def _model_output(msg: Any) -> str:
        local_dict = {"exp_time": exp_time, "uuid4": uuid4}
        return pydantic_model_to_py_code(
            msg_to_pydantic_model(
                msg,
                parse_msg_desc_method=demo_pb2,
                local_dict=local_dict
            ),
        )

    def test_user_message(self) -> None:
        assert """
class SexType(IntEnum):
    man = 0
    women = 1


class ExampleProtoCommonSingleDemoEnum(IntEnum):
    \"\"\"Note: The current class does not belong to the package
    ExampleProtoCommonSingleDemoEnum protobuf path:example_proto/common/single.proto\"\"\"

    zero = 0
    one = 1
    two = 3


class ExampleProtoCommonSingleDemoMessage(BaseModel):
    \"\"\"Note: The current class does not belong to the package
    ExampleProtoCommonSingleDemoMessage protobuf path:example_proto/common/single.proto\"\"\"

    earth: str = FieldInfo(default="")
    mercury: str = FieldInfo(default="")
    mars: str = FieldInfo(default="")


class UserMessage(BaseModel):
    uid: str = FieldInfo(title="UID", description="user union id", example="10086")
    age: int = FieldInfo(default=0, title="use age", ge=0, example=18)
    height: float = FieldInfo(default=0.0, ge=0, le=2)
    sex: SexType = FieldInfo(default=0)
    demo: ExampleProtoCommonSingleDemoEnum = FieldInfo(default=0)
    is_adult: bool = FieldInfo(default=False)
    user_name: str = FieldInfo(default="", description="user name", min_length=1, max_length=10, example="so1n")
    demo_message: ExampleProtoCommonSingleDemoMessage = FieldInfo()
""" in self._model_output(demo_pb2.UserMessage)

    def test_map_message(self) -> None:
            assert """
class SexType(IntEnum):
    man = 0
    women = 1


class ExampleProtoCommonSingleDemoEnum(IntEnum):
    \"\"\"Note: The current class does not belong to the package
    ExampleProtoCommonSingleDemoEnum protobuf path:example_proto/common/single.proto\"\"\"

    zero = 0
    one = 1
    two = 3


class ExampleProtoCommonSingleDemoMessage(BaseModel):
    \"\"\"Note: The current class does not belong to the package
    ExampleProtoCommonSingleDemoMessage protobuf path:example_proto/common/single.proto\"\"\"

    earth: str = FieldInfo(default="")
    mercury: str = FieldInfo(default="")
    mars: str = FieldInfo(default="")


class UserMessage(BaseModel):
    uid: str = FieldInfo(title="UID", description="user union id", example="10086")
    age: int = FieldInfo(default=0, title="use age", ge=0, example=18)
    height: float = FieldInfo(default=0.0, ge=0, le=2)
    sex: SexType = FieldInfo(default=0)
    demo: ExampleProtoCommonSingleDemoEnum = FieldInfo(default=0)
    is_adult: bool = FieldInfo(default=False)
    user_name: str = FieldInfo(default="", description="user name", min_length=1, max_length=10, example="so1n")
    demo_message: ExampleProtoCommonSingleDemoMessage = FieldInfo()


class MapMessage(BaseModel):
    user_map: typing.Dict[str, UserMessage] = FieldInfo(default_factory=dict)
    user_flag: typing.Dict[str, bool] = FieldInfo(default_factory=dict)
""" in self._model_output(demo_pb2.MapMessage)

    def test_repeated_message(self) -> None:
            assert """
class SexType(IntEnum):
    man = 0
    women = 1


class ExampleProtoCommonSingleDemoEnum(IntEnum):
    \"\"\"Note: The current class does not belong to the package
    ExampleProtoCommonSingleDemoEnum protobuf path:example_proto/common/single.proto\"\"\"

    zero = 0
    one = 1
    two = 3


class ExampleProtoCommonSingleDemoMessage(BaseModel):
    \"\"\"Note: The current class does not belong to the package
    ExampleProtoCommonSingleDemoMessage protobuf path:example_proto/common/single.proto\"\"\"

    earth: str = FieldInfo(default="")
    mercury: str = FieldInfo(default="")
    mars: str = FieldInfo(default="")


class UserMessage(BaseModel):
    uid: str = FieldInfo(title="UID", description="user union id", example="10086")
    age: int = FieldInfo(default=0, title="use age", ge=0, example=18)
    height: float = FieldInfo(default=0.0, ge=0, le=2)
    sex: SexType = FieldInfo(default=0)
    demo: ExampleProtoCommonSingleDemoEnum = FieldInfo(default=0)
    is_adult: bool = FieldInfo(default=False)
    user_name: str = FieldInfo(default="", description="user name", min_length=1, max_length=10, example="so1n")
    demo_message: ExampleProtoCommonSingleDemoMessage = FieldInfo()


class RepeatedMessage(BaseModel):
    str_list: typing.List[str] = FieldInfo(default_factory=list, min_items=3, max_items=5)
    int_list: typing.List[int] = FieldInfo(default_factory=list, min_items=1, max_items=5, unique_items=True)
    user_list: typing.List[UserMessage] = FieldInfo(default_factory=list)
""" in self._model_output(demo_pb2.RepeatedMessage)

    def test_nested_message(self) -> None:
            assert """
class SexType(IntEnum):
    man = 0
    women = 1


class ExampleProtoCommonSingleDemoEnum(IntEnum):
    \"\"\"Note: The current class does not belong to the package
    ExampleProtoCommonSingleDemoEnum protobuf path:example_proto/common/single.proto\"\"\"

    zero = 0
    one = 1
    two = 3


class ExampleProtoCommonSingleDemoMessage(BaseModel):
    \"\"\"Note: The current class does not belong to the package
    ExampleProtoCommonSingleDemoMessage protobuf path:example_proto/common/single.proto\"\"\"

    earth: str = FieldInfo(default="")
    mercury: str = FieldInfo(default="")
    mars: str = FieldInfo(default="")


class UserMessage(BaseModel):
    uid: str = FieldInfo(title="UID", description="user union id", example="10086")
    age: int = FieldInfo(default=0, title="use age", ge=0, example=18)
    height: float = FieldInfo(default=0.0, ge=0, le=2)
    sex: SexType = FieldInfo(default=0)
    demo: ExampleProtoCommonSingleDemoEnum = FieldInfo(default=0)
    is_adult: bool = FieldInfo(default=False)
    user_name: str = FieldInfo(default="", description="user name", min_length=1, max_length=10, example="so1n")
    demo_message: ExampleProtoCommonSingleDemoMessage = FieldInfo()


class RepeatedMessage(BaseModel):
    str_list: typing.List[str] = FieldInfo(default_factory=list, min_items=3, max_items=5)
    int_list: typing.List[int] = FieldInfo(default_factory=list, min_items=1, max_items=5, unique_items=True)
    user_list: typing.List[UserMessage] = FieldInfo(default_factory=list)


class MapMessage(BaseModel):
    user_map: typing.Dict[str, UserMessage] = FieldInfo(default_factory=dict)
    user_flag: typing.Dict[str, bool] = FieldInfo(default_factory=dict)


class NestedMessageUserPayMessage(BaseModel):
    bank_number: PaymentCardNumber = FieldInfo(default="")
    exp: datetime = FieldInfo(default_factory=exp_time)
    uuid: str = FieldInfo(default_factory=uuid4)


class IncludeEnum(IntEnum):
    zero = 0
    one = 1
    two = 2


class NestedMessage(BaseModel):
    user_list_map: typing.Dict[str, RepeatedMessage] = FieldInfo(default_factory=dict)
    user_map: typing.Dict[str, MapMessage] = FieldInfo(default_factory=dict)
    user_pay: NestedMessageUserPayMessage = FieldInfo()
    include_enum: IncludeEnum = FieldInfo(default=0)
    empty: None = FieldInfo()
""" in self._model_output(demo_pb2.NestedMessage)


class TestTextCommentByPyi(BaseTestTextComment):
    @staticmethod
    def _model_output(msg: Any) -> str:
        local_dict = {"exp_time": exp_time, "uuid4": uuid4}
        return pydantic_model_to_py_code(
            msg_to_pydantic_model(
                msg,
                parse_msg_desc_method=demo_pb2,
                local_dict=local_dict
            ),
        )


class TestTextCommentByProtobufFProtobufField(BaseTestTextComment):
    @staticmethod
    def _model_output(msg: Any) -> str:
        local_dict = {"exp_time": exp_time, "uuid4": uuid4}
        from pathlib import Path
        if not Path("example").exists():
            # ignore exec in github action runner
            return pydantic_model_to_py_code(
                msg_to_pydantic_model(
                    msg,
                    parse_msg_desc_method=demo_pb2,
                    local_dict=local_dict
                ),
            )
        return pydantic_model_to_py_code(
            msg_to_pydantic_model(
                msg,
                parse_msg_desc_method="example",
                local_dict=local_dict
            ),
        )
