from langchain_core import messages
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

# 定义模型
model = ChatOpenAI(model="deepseek-chat")

# 定义工具
tool = TavilySearch(tavily_api_key="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",max_results = 4)

# 绑定工具
model_with_tools = model.bind_tools([tool])

# 定义消息列表
messages = [
    HumanMessage("洛阳2026年7月2日天气如何")
]

ai_msg = model_with_tools.invoke(messages)
# 返回AI使用的工具列表,主要看tool_calls
messages.append(ai_msg)

for tool_call in ai_msg.tool_calls:

    # 得到工具返回的结果
    tool_msg = tool.invoke(tool_call)
    messages.append(tool_msg)

# 进行数据的整合
print(model.invoke(messages).content)