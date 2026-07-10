from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import CharacterTextSplitter

md_loader = UnstructuredMarkdownLoader(
    file_path="../../Docs/markdown/脚手架级微服务租房平台Q&A.md",
)

data = md_loader.load()


text_splitter = CharacterTextSplitter(
    separator="\n\n",       #分隔符，一般来说，有一个默认的分隔符优先级列表:["\n\n","\n"," "]
    chunk_size=380,         # 块大小 (参考标准，为了保证段落/句子完整，会超出此设定的大小)
    chunk_overlap=20,       # 块重叠大小
    length_function=len,    #测量字符长度的函数
    is_separator_regex=False,#是否正则表达式描写分隔符吗？
)


documents = text_splitter.split_documents(data)
for document in documents[:10]:
    print("*" * 30)
    print(document)