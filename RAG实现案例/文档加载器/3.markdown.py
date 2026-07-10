from langchain_community.document_loaders import UnstructuredMarkdownLoader

md_loader = UnstructuredMarkdownLoader(

    file_path="../../Docs/markdown/脚手架级微服务租房平台Q&A.md",
    # mode="single"                #MD加载器默认将文档加载为一个
    mode="elements"                #拆分成不同子块

)

docs = md_loader.load()


print(f"MD文档总数: \n{len(docs)}\n")


print(f"MD文档总数：\n{len(docs)}\n")
print(f"第一个文档的内容是：\n{docs[0].page_content}\n")
# 'source': '../Docs/markdown/脚手架级微服务租房平台Q&A.md'
# 'category': 'Title',                              # 分类
# 'element_id': '3a0670f9bfd58576e430ef11def41593'  # 每个文档的唯一标识
# print(f"第一个文档的元数据字典是：\n{docs[0].metadata}\n")

# print(f"第二个文档的内容是：\n{docs[1].page_content}\n")
# # 'source': '../Docs/markdown/脚手架级微服务租房平台Q&A.md'
# # 'parent_id': '3a0670f9bfd58576e430ef11def41593',
# # 'category': 'Title',
# # 'element_id': 'fcb08b2a85942455eecebb9467ffca4c'
# print(f"第二个文档的元数据字典是：\n{docs[1].metadata}\n")

# print(f"第三个文档的内容是：\n{docs[2].page_content}\n")
# # 'source': '../Docs/markdown/脚手架级微服务租房平台Q&A.md'
# # 'parent_id': 'fcb08b2a85942455eecebb9467ffca4c',
# # 'category': 'UncategorizedText',                    # 未分类文本
# # 'element_id': 'a6fc0b5a457d21234bf1c4a6ae0a18db'
# print(f"第三个文档的元数据字典是：\n{docs[2].metadata}\n")
#
# # {
# # 'Table',            表格
# # 'Image',            图像
# # 'NarrativeText',    叙事性文本
# # 'Title',            标题
# # 'ListItem',         列表项
# # 'UncategorizedText' 未分类的文本
# # }
# print(f"当前MD文档的所有分类：{set(document.metadata["category"] for document in docs)}")