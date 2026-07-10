from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import  RecursiveCharacterTextSplitter

md_loader = UnstructuredMarkdownLoader(
    file_path="../../Docs/markdown/脚手架级微服务租房平台Q&A.md",
)

data = md_loader.load()


# tiktoken 分词器
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    separators=["\n\n","\n"," "],
    chunk_size=400,              # 块token大小(参考标准，为了保证段落/句子完整，会超出此设定的大小)
    chunk_overlap=50,            # 块重叠大小
    is_separator_regex=False     # 是否正则表达式描写分隔符吗？
)

documents = text_splitter.split_documents(data)
for document in documents[:10]:
    print("*" * 30)
    print(document)