from langchain_community.chat_models import ChatZhipuAI
from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_redis import RedisConfig, RedisVectorStore
# 构建链：完成Rag能力


# 定义组件，构建链


# 嵌入模型
embeddings= ZhipuAIEmbeddings(
    model="embedding-3"
)

# 聊天模型
model =ChatZhipuAI(model="glm-4-flash")

# 1.先从知识库中检索


# Redis配置
config = RedisConfig(
    index_name="qa",  # 定义索引名
    redis_url="redis://127.0.0.1:6379",
    metadata_schema=[
        {"name": "category", "type": "tag"},   # 添加索引字段：分类
        {"name": "num", "type": "numeric"},    # 添加索引字段：编号
    ]
)
# 向量库
vector_store = RedisVectorStore(
    embeddings=embeddings,
    config=config,
)

# 检索器
retriever = vector_store.as_retriever()

# 2.将检索结果+查询语句 构建为提示词(提示词模板)

# 提示词模板
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "human",
            """你是负责回答问题的助手。使用一下检索到的上下文片段来回答问题。如果你不知道答案，就说不知道答案。最多回复三句话的结果，回答要简明扼要
            Question:{question}
            Context:{context}
            Answer:"""
        )
    ]
)


# 将检索出来的文档转换为文本传递给提示词模板
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 3.将消息发送给LLM(实例化消息，交由链来完成)

# 定义链
chain = (
    {"context": retriever | format_docs , "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()  # 输出解析器
)


# 4.打印字符串结果(流式)
for chunk in chain.stream("介绍一下这个项目"):
    print(chunk,end="",flush=True)












