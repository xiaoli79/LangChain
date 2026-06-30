from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# 定义模型
model = ChatOpenAI(
    model="deepseek-chat",
    # 温度范围是0~2 ~~ 温度越高，AI回复的内容天马行空温度越低，答案越保护
    # 0.1 ~0.5 轻微变化~~ 技术文档、写作
    # 0.5~1    平衡创意~~ 对话、稍微创意的写作
    temperature=1,

    # 输出最大token数
    # Token是文本的基本单位
    # token不是完全等同与一个词或一个字
    # max_tokens= 10,

    # 是否有超时时间
    # timeout=None,

    # 请求失败最大请求数
    # max_retries=2,

    # 模型的相关key
    # api_key="",

    # 基本路径
    # base_url="",

    # 组织ID
    # organization="",
)

# 自定义消息
messages = [
    SystemMessage(content="请帮我补全一段故事，100字以内"),
    HumanMessage(content="一只闫路甲正在干什么")
]

# .定义输出解析
parser = StrOutputParser()

chain = model | parser

print(chain.invoke(messages))