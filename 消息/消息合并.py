from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, merge_message_runs

# 定义大模型
model = ChatOpenAI(model="gpt-4o-mini")

# 历史消息记录
messages = [
    SystemMessage("你是一个聊天助手。"),
    SystemMessage("你总是以笑话回应。"),
    HumanMessage("为什么要使用 LangChain?"),
    HumanMessage("为什么要使用 LangGraph?"),
    AIMessage("因为当你试图让你的代码更有条理时，LangGraph 会让你感到“节点”是个好主意！"),
    AIMessage("不过别担心，它不会“分散”你的注意力！"),
    HumanMessage("选择LangChain还是LangGraph?"),
]

merged = merge_message_runs(messages)
# # 打印合并后的每个消息
# # print("\n".join([repr(x) for x in merged]))
# print(merged)

print(model.invoke(merged))