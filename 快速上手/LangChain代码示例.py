from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


# 显式指定 base_url，强行把方向盘打向 DeepSeek
model = ChatOpenAI(
    model="deepseek-chat",                  # 模型名字没问题                    # 传入你的 Key
)

# 自定义消息
messages = [
    SystemMessage(content="请帮我进行翻译，由中文翻译成英文"),
    HumanMessage(content="我是闫路甲他爹，我是闫路甲他爷爷")
]

# 调用并打印
# result = model.invoke(messages)
# print(result)

# .定义输出解析
parser = StrOutputParser()
# print(parser.invoke(result))

# 定义链
chain = model | parser
# 执行链  所有执行的动作全部交给链条来进行执行
print(chain.invoke(messages))
