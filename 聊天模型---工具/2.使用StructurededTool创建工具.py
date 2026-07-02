from typing import Tuple, List

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


# 方式一
# 工具 Schema 不能缺失工具名、工具描述、工具参数
# def add(a:int , b :int) -> int:
#     """两数相加"""
#     return a + b
#
#
# add_tool =  StructuredTool.from_function(func=add)
# print(add_tool.invoke({"a" : 2,"b" : 6}))


# 方式二
# class AddInput(BaseModel):
#     a: int = Field(description="第一个整数")
#     b: int = Field(description="第二个整数")
#
#
# def add(a:int , b :int) -> int:
#     """两数相加"""
#     return a + b
#
#
# add_tool =  StructuredTool.from_function(
#     func=add,
#     name="ADD",
#     description="两数相加",
#     args_schema=AddInput,
#
# )
# print(add_tool.invoke({"a" : 2,"b" : 6}))


# 方式三 使用大模型来输出其相应的过程
class AddInput(BaseModel):
    a: int = Field(description="第一个整数")
    b: int = Field(description="第二个整数")


def add(a:int , b :int) -> Tuple[str,List[int]]:
    """两数相加"""
    nums = [a,b]
    content = f"{nums}相加的结果是{a+b}"
    return content,nums


add_tool =  StructuredTool.from_function(
    func=add,
    name="ADD",
    description="两数相加",
    args_schema=AddInput,
    response_format="content_and_artifact"

)


# 模拟大模型调用姿势
print(add_tool.invoke(
    {
        "name": "ADD",
        "args":{"a" : 3, "b" : 4},
        "type": "tool_call",   # 必填
        "id": "111"  # 必填，用来将工具调用请求和结果关联起来
    }
))
















