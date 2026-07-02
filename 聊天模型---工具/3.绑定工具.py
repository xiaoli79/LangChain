from typing import Annotated

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


@tool
def add(
        a: Annotated[int,...,"第一个整数"],
        b: Annotated[int,...,"第二个整数"]
) -> int:
    """两数相加"""
    return a + b


@tool
def multiply(
        a: Annotated[int,...,"第一个整数"],
        b: Annotated[int,...,"第二个整数"]
) -> int:
    """两数相乘"""
    return a * b


model = ChatOpenAI(model="deepseek-chat")

# 工具绑定
tools = [add,multiply]
model_with_tools = model.bind_tools(tools,tool_choice="any")


# 工具调用
print(model_with_tools.invoke("6+6等于多少"))