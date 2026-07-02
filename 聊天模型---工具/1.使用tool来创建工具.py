from typing import Annotated

from langchain_core.tools import tool
from pydantic import BaseModel, Field


# 法一
# # 定义工具
# @tool
# def add(a: int,b: int) -> int:
#     # 这个文档字符串是必须要写的~~
#     """
#     两数相加
#     :param a:  a 代表第一个整数
#     :param b:  b 代表第二个整数
#     :return:
#     """
#     return a+b


# 第二种方式
# class AddInput(BaseModel):
#
#     """两数相加 """
#     a: int = Field(...,description= "第一个整数")
#     b: int = Field(...,description= "第二个整数")
#
# @tool(args_schema=AddInput)
# def add(a: int,b: int) -> int:
#     return a+b


# 第三种方式
@tool
def add(
        a : Annotated[int,...,"第一个整数"],
        b : Annotated[int,...,"第二个整数"]
) -> int:
    # 这个文档字符串是必须要写的~~
    """
    两数相加
    :param a:  a 代表第一个整数
    :param b:  b 代表第二个整数
    :return:
    """
    return a+b

print(add.invoke({"a":2,"b":3}))
print(add.name)
print(add.description)
print(add.args)

