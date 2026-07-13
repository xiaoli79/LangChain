from langchain_community.embeddings import ZhipuAIEmbeddings

# 定义嵌入模型
embeddings = ZhipuAIEmbeddings(
    model="embedding-3"
)

query_vector = embeddings.embed_query("你好")

print(f"embedding-3 向量维度：{len(query_vector)}")

print(f"向量前五个数值:{query_vector[:5]}")