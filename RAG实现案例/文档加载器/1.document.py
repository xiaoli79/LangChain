
from langchain_core.documents import Document



# 手动定义的文档列表
documents = [
    Document(
        # 内容
        page_content="狗是忠实的伴侣",
        # 元数据属性可以包含：文档源，与其他文档的关系以及其他属性信息
        metadata = {"source" : "pets-doc"}
    )
]








































