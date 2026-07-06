from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, filter_messages
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")


messages = [
    SystemMessage("你是一个聊天助手", id="1"),
    HumanMessage("示例输入", id="2"),
    AIMessage("示例输出", id="3"),
    HumanMessage("真实输入", id="4"),
    AIMessage("真实输出", id="5"),
]


#按照类型筛选
# print(filter_messages(include_types ="human").invoke(messages))
# print(filter_messages(messages, include_types="human"))

#按照id筛选
print(filter_messages(messages, exclude_ids=["3"]))