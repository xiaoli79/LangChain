from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")

# model.invoke("我是小明！你好").pretty_print()

# # 模拟信息列表，让模型具有记忆能力
# messages = [
#     HumanMessage(content="我是小明，你好！！"),
#     AIMessage(content="你好，小明！很高兴认识你！今天你有什么想聊呢"),
#     HumanMessage(content="你知道我是谁吗？")
# ]
#
# model.invoke(messages).pretty_print()

store = {}

# 根据会话id 查询会话里的消息列表
def get_session_history(session_id: str) -> BaseChatMessageHistory :
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 包装了model，让model具备存储历史消息的能力
with_history_message_model = RunnableWithMessageHistory(model,get_session_history)

config = {"configurable" :{"session_id" : "1"}}

with_history_message_model.invoke([HumanMessage(content="我是小明，你好！")], config=config).pretty_print()

with_history_message_model.invoke([HumanMessage(content="大胆，你知道我是谁吗？")], config=config).pretty_print()
