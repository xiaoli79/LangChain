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
# LCEL其实是一种编排解决方案，它可以使用LangChain能够以优化的方式处理链的运行时执行。任何
# 两个Runnable实例都可以在“链”上一起成序列。上一个可运行对象的.invoke()调用的输出作为输入
# 传递给下一个可运行对象。方法就是使用 |
# 第一种方式
chain = model | parser
# 第二种方式
# chain = RunnableSequence(first= model,last = parser)
# 第三种方式
# chain = model.pipe(chain)
# 执行链  所有执行的动作全部交给链条来进行执行
print(chain.invoke(messages))
