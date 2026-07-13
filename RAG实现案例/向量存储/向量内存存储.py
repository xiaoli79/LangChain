from xml.dom.minidom import Document

from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import CharacterTextSplitter
from langchain_zhipu import ZhipuAIEmbeddings

# 定义嵌入式模型
embeddings = ZhipuAIEmbeddings(
    model="embedding-3"
)
# 内存向量存储
vector_store = InMemoryVectorStore(embedding = embeddings)

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

# 存储文档到内存向量存储中
# add_documents: 将要存储的文档列表进行编排索引
ids = vector_store.add_documents(docs)

print(f"共有{len(docs)}个文档，编排了{len(ids)}个索引")
print(f"前三个文档的索引:{ids[:3]}")

# 根据索引获取文档
# doc_2 = vector_store.get_by_ids(ids[:2])
# print(doc_2)
# [Document(id='c93cff79-7460-4863-bc73-03c4c0eb0336', metadata={'source': '../../Docs/markdown/脚手架级微服务租房平台Q&A.md', 'category_depth': 0, 'languages': ['zho'], 'file_directory': '../../Docs/markdown', 'filename': '脚手架级微服务租房平台Q&A.md', 'filetype': 'text/markdown', 'last_modified': '2026-07-10T11:19:10', 'category': 'Title', 'element_id': '3a0670f9bfd58576e430ef11def41593'}, page_content='通用问题'),
# Document(id='10454606-ceb7-42a7-b609-9ab124bfce96', metadata={'source': '../../Docs/markdown/脚手架级微服务租房平台Q&A.md', 'category_depth': 2, 'emphasized_text_contents': ['为什么做这个项目？'], 'emphasized_text_tags': ['b'], 'languages': ['zho'], 'file_directory': '../../Docs/markdown', 'filename': '脚手架级微服务租房平台Q&A.md', 'filetype': 'text/markdown', 'last_modified': '2026-07-10T11:19:10', 'parent_id': '3a0670f9bfd58576e430ef11def41593', 'category': 'Title', 'element_id': 'fcb08b2a85942455eecebb9467ffca4c'}, page_content='为什么做这个项目？')]

# 删除文档
# vector_store.delete(ids[:2])

# 获取前三个文档
# doc_3 = vector_store.get_by_ids(ids[:3])
# print(doc_3)
# [Document(id='e13ca375-9c82-44be-ac7c-5b4c953e499b', metadata={'source': '../../Docs/markdown/脚手架级微服务租房平台Q&A.md', 'category_depth': 1, 'emphasized_text_contents': ['回答1：（出于兴趣爱好开发）'], 'emphasized_text_tags': ['b'], 'languages': ['zho'], 'file_directory': '../../Docs/markdown', 'filename': '脚手架级微服务租房平台Q&A.md', 'filetype': 'text/markdown', 'last_modified': '2026-07-10T11:19:10', 'parent_id': 'fcb08b2a85942455eecebb9467ffca4c', 'category': 'ListItem', 'element_id': 'a6fc0b5a457d21234bf1c4a6ae0a18db'}, page_content='回答1：（出于兴趣爱好开发）')]




# 元数据的过滤
def _filter_function(doc: Document) -> bool:
    return doc.metadata.get("source") == "../../Docs/markdown/脚手架级微服务租房平台Q&A.md"

# 检索
# similarity_search：根据余弦相似度来捕捉语义的
search_docs = vector_store.similarity_search(
    query="项目介绍",
    k=2,
    filter=_filter_function
)

for doc in search_docs:
    print("*" * 30)
    print(doc.page_content)
























