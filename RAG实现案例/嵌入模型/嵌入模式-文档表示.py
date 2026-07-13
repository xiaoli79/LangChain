from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

embeddings = ZhipuAIEmbeddings(
    model="embedding-3"
)
md_loader = UnstructuredMarkdownLoader(

    file_path="../../Docs/markdown/脚手架级微服务租房平台Q&A.md",
    mode="single"                #MD加载器默认将文档加载为一个
    #mode="elements"                #拆分成不同子块
)

docs = md_loader.load()



# tiktoken 分词器
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base", # cl100k_base 是tiktoken 分词器中的一种编码方式
    chunk_size=400,              # 块token大小(参考标准，为了保证段落/句子完整，会超出此设定的大小)
    chunk_overlap=50,            # 块重叠大小
)

# 将文档列表表示为向量列表~
texts = [doc.page_content for doc in docs]
docs_vector = embeddings.embed_documents(texts)

print(f"文档数量:{len(docs)},转换的向量列表数量:{len(docs_vector)}")
print(f"第一个文档向量维度:{len(docs_vector[0])}")
print(f"第一个文档向量前五个值:{docs_vector[0][:5]}")

