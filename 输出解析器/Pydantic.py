from typing import Optional

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_zhipu import ChatZhipuAI
from pydantic import BaseModel, Field

model = ChatZhipuAI(
    model="glm-4", # 确保小写
)
# Pydantic 对象
class Joke(BaseModel):
    """给用户讲的一个笑话"""

    setup: str = Field(description="这个笑话的开头")
    punchline: str = Field(description="这个笑话的妙语")
    rating: Optional[int] = Field(default=None, description="从1-10分，给这个笑话评分")

# 定义解析器
parser = PydanticOutputParser(pydantic_object=Joke)
# print(parser.get_format_instructions())

prompt = PromptTemplate(
    template="回复用户问题.\n返回结构说明: {format_instructions}\n用户问题:{query}\n",
    partial_variables={"format_instructions": parser.get_format_instructions()},
    input_variables=["query"],
)


# print(prompt.invoke({"query" : "讲一个关于跳舞的笑话"}))

chain = prompt | model | parser

print(chain.invoke({"query": "讲一个关于跳舞的笑话"}))


