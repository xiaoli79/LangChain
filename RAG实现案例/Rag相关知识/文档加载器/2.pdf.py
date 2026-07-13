from langchain_community.document_loaders import PyPDFLoader

# 加载pdf总数
# pdf加载器并不能识别图片中的内容
loader = PyPDFLoader(file_path="../../../Docs/pdf/脚手架级微服务租房平台Q&A.pdf")
docs = loader.load()

print(f"PDF文档总数: {len(docs)}\n")

print(f"第一页文本的内容(前200)是：\n{docs[0].page_content[:200]}\n")
print(f"第一页的元数据字典是：\n{docs[0].metadata}\n")
print(f"第二页文本的内容(前200)是：\n{docs[1].page_content[:200]}\n")
print(f"第二页的元数据字典是：\n{docs[1].metadata}\n")
# PDF加载器将文本加载进来了，图片呢？
print(f"第三页文本的内容(前200)是：\n{docs[2].page_content[:200]}\n")
print(f"第三页的q元数据字典是：\n{docs[2].metadata}\n")