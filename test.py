from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
# 1. 引入智谱专属的组件
from langchain_zhipu import ChatZhipuAI

# 定义模型
model = ChatZhipuAI(
    model="glm-4-flash", # 确保小写
    # temperature=1,
)

# 自定义消息
messages = [
    # SystemMessage(content="请帮我补全一段故事，100字以内"),
    HumanMessage(content="你是谁")
]

# 定义输出解析
parser = StrOutputParser()

chain = model | parser

# 3. 再次运行测试
print(chain.invoke(messages))