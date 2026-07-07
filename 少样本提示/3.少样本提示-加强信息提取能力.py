from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.utils.function_calling import tool_example_to_messages
from langchain_openai import ChatOpenAI
from typing import Optional, List
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatOpenAI(model = "gpt-4o-mini")

# 1. 定义结构化输出
class Person(BaseModel):
    """一个人的信息。"""
    # 注意:
    # 1. 每个字段都是 Optional “可选的” —— 允许 LLM 在不知道答案时输出 None。
    # 2. 每个字段都有一个 description “描述” —— LLM使用这个描述。
    # 有一个好的描述可以帮助提高提取结果。
    name: Optional[str] = Field(default=None, description="这个人的名字")
    hair_color: Optional[str] = Field(default=None, description="如果知道这个人头发的颜色")
    skin_color: Optional[str] = Field(default=None, description="如果知道这个人的肤色")
    height_in_meters: Optional[str] = Field(default=None, description="以米为单位的高度")



class Data(BaseModel):
    """人员列表数据"""
    people: List[Person] = Field(description="人员列表")


# 2.定义示例(不是 Message)
examples = [
    (
        "海洋是广阔的、蓝色的。它有两万多英尺深",
        Data(people=[]),
    ),
    (
        "小明在跳舞,1米78的身高看起来很灵活",
        Data(people=[
            Person(name='小明', hair_color=None, skin_color=None, height_in_meters='1.78'),
        ]),
    ),
]


# 3. 定义提示词模板
prompt_template = ChatPromptTemplate(
    [
        SystemMessage(content="你是一个提取信息的专家，只从文本中提取相关信息。如果您不知道要提取的属性的值，属性值返回null"),
        MessagesPlaceholder("example_messages"), # 消息占位符，将示例转换为Message后插入进来
        ("user", "{new_message}"),
    ]
)



example_messages =[]

# 将示例转换为Messages
for txt,tool_call in examples:
    if tool_call.people:
        ai_response = "检测到人"
    else:
        ai_response = "未检测到人"

    example_messages.extend(tool_example_to_messages(
        txt, # 示例的输入
        [tool_call], #工具 (Data(people=[]) 准确的参考标准)
        ai_response=ai_response, #让LLM强制返回ai_response
    ))
# [

# 第一个示例
# HumanMessage(content='海洋是广阔的、蓝色的。它有两万多英尺深', additional_kwargs={}, response_metadata={}),
# AIMessage(content='', additional_kwargs={'tool_calls': [{'id': '0e7222d0-a470-4f19-a2b1-a8860d92e43b', 'type': 'function', 'function': {'name': 'Data', 'arguments': '{"people":[]}'}}]}, response_metadata={}, tool_calls=[{'name': 'Data', 'args': {'people': []}, 'id': '0e7222d0-a470-4f19-a2b1-a8860d92e43b', 'type': 'tool_call'}], invalid_tool_calls=[]),
# ToolMessage(content='You have correctly called this tool.', tool_call_id='0e7222d0-a470-4f19-a2b1-a8860d92e43b'),
# AIMessage(content='未检测到人', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),

# 第二个示例
# HumanMessage(content='小明在跳舞,1米78的身高看起来很灵活', additional_kwargs={}, response_metadata={}),
# AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'e5c2f74f-c5ec-4021-a34b-abcd4c6f6a5c', 'type': 'function', 'function': {'name': 'Data', 'arguments': '{"people":[{"name":"小明","hair_color":null,"skin_color":null,"height_in_meters":"1.78"}]}'}}]}, response_metadata={}, tool_calls=[{'name': 'Data', 'args': {'people': [{'name': '小明', 'hair_color': None, 'skin_color': None, 'height_in_meters': '1.78'}]}, 'id': 'e5c2f74f-c5ec-4021-a34b-abcd4c6f6a5c', 'type': 'tool_call'}], invalid_tool_calls=[]),
# ToolMessage(content='You have correctly called this tool.', tool_call_id='e5c2f74f-c5ec-4021-a34b-abcd4c6f6a5c'),
# AIMessage(content='检测到人', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]
print(example_messages)

# 5. 定义的结构化模型
# structured_model = model.with_structured_output(schema=Data)

# 6. 定义链(没有强制结构化输出)
# messages=[
# SystemMessage(content='你是一个提取信息的专家，只从文本中提取相关信息。如果您不知道要提取的属性的值，属性值返回null', additional_kwargs={}, response_metadata={}),

# 第一个示例
# HumanMessage(content='海洋是广阔的、蓝色的。它有两万多英尺深', additional_kwargs={}, response_metadata={}),
# AIMessage(content='', additional_kwargs={'tool_calls': [{'id': '7faf6d44-692d-4de6-99e3-1d4fef5a41f0', 'type': 'function', 'function': {'name': 'Data', 'arguments': '{"people":[]}'}}]}, response_metadata={}, tool_calls=[{'name': 'Data', 'args': {'people': []}, 'id': '7faf6d44-692d-4de6-99e3-1d4fef5a41f0', 'type': 'tool_call'}], invalid_tool_calls=[]),
# ToolMessage(content='You have correctly called this tool.', tool_call_id='7faf6d44-692d-4de6-99e3-1d4fef5a41f0'),
# AIMessage(content='未检测到人', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),

# 第二个示例
# HumanMessage(content='小明在跳舞,1米78的身高看起来很灵活', additional_kwargs={}, response_metadata={}),
# AIMessage(content='', additional_kwargs={'tool_calls': [{'id': '3c772fb1-bf2c-42a0-b453-b19215877349', 'type': 'function', 'function': {'name': 'Data', 'arguments': '{"people":[{"name":"小明","hair_color":null,"skin_color":null,"height_in_meters":"1.78"}]}'}}]}, response_metadata={}, tool_calls=[{'name': 'Data', 'args': {'people': [{'name': '小明', 'hair_color': None, 'skin_color': None, 'height_in_meters': '1.78'}]}, 'id': '3c772fb1-bf2c-42a0-b453-b19215877349', 'type': 'tool_call'}], invalid_tool_calls=[]),
# ToolMessage(content='You have correctly called this tool.', tool_call_id='3c772fb1-bf2c-42a0-b453-b19215877349'),
# AIMessage(content='检测到人', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),

# 第三个示例
# HumanMessage(content='篮球场上，身高两米的中锋王伟默契地将球传给一米七的后卫挚友李明，完成一记绝杀。这对老友用十年配合弥补了身高的差距。', additional_kwargs={}, response_metadata={})]


# print(prompt_template.invoke({
#         "example_messages": example_messages,
#         "new_message": "篮球场上，身高两米的中锋王伟默契地将球传给一米七的后卫挚友李明，完成一记绝杀。这对老友用十年配合弥补了身高的差距。"
# }))

# chain = prompt_template | structured_model
# print(chain.invoke(
#     {
#         "example_messages": example_messages,
#         "new_message": "篮球场上，身高两米的中锋王伟默契地将球传给一米七的后卫挚友李明，完成一记绝杀。这对老友用十年配合弥补了身高的差距。"
#     }
# ))

# 虽然结果准确，但我们可以通过示例加强信息提取的准确度








































