from typing import Annotated

from langchain_core.messages import HumanMessage
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
# model = ChatDeepSeek(model="deepseek-chat")

# 工具绑定
tools = [add,multiply]
model_with_tools = model.bind_tools(tools,tool_choice="any")

# 定义消息列表，添加要传递给聊天模型的消息
# 用户提示词
message = [
    HumanMessage("6+ 6等于多少?,3* 3等于多少?")
]

# 工具调用
ai_msg = model_with_tools.invoke(message)
message.append(ai_msg)
# 这是AI返回的信息，是为了告诉你调用了哪些工具,主要是看tool_calls
print(ai_msg)

# 构造ToolMessage，并添加到消息列表中去
for tool_call in ai_msg.tool_calls:
    selected_tool = {"add": add , "multiply": multiply }[tool_call["name"].lower()]

    # 这里面是从调用工具进而得出结果,例如3 * 3 = 9 ，这里面的tool_msg  = 9
    tool_msg = selected_tool.invoke(tool_call)
    message.append(tool_msg)


print(message)
# 然后由AI将用户提示词,AI返回的信息(即相关的工具),工具返回的答案进行进而,经过AI工作,进而得出组装后的信息.
print(model.invoke(message).content)