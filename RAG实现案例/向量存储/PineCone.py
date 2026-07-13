from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import CharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone()
index_name = "qa"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=2048,  # ZhipuAI embedding-3 的输出维度，请查智谱文档确认
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1",
        ),
    )

index = pc.Index(index_name)

embeddings = ZhipuAIEmbeddings(model="embedding-3")

vector_store = PineconeVectorStore(
    embedding=embeddings,
    index=index,
)

md_loader = UnstructuredMarkdownLoader(

    file_path="../../Docs/markdown/脚手架级微服务租房平台Q&A.md",
    mode="single"                #MD加载器默认将文档加载为一个
)

docs = md_loader.load()

# tiktoken 分词器
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base", # cl100k_base 是tiktoken 分词器中的一种编码方式
    chunk_size=400,              # 块token大小(参考标准，为了保证段落/句子完整，会超出此设定的大小)
    chunk_overlap=50,            # 块重叠大小
)

docs = text_splitter.split_documents(docs)

# 文档列表
for i,doc in enumerate(docs,start=1):
    doc.metadata["category"] = "QA"
    doc.metadata["num"] = i


# CRUD,检索

# 新增
# ids = vector_store.add_documents(documents=docs)
# print(f"编制了{len(ids)}个索引")
# print(f"前三个索引是:{ids[:3]}")

# 全量删除
# vector_store.index.delete(drop=True)

# 查询



# search_docs = vector_store.similarity_search(query="项目介绍", k=2)
# for doc in search_docs:
#     print("*" * 30)
#     print(f"文档内容：{doc.page_content}")
#     print(f"文档元数据：{doc.metadata}")