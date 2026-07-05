from typing import Optional, List
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


model = ChatOpenAI(model= "gpt-4o-mini")

class Joke(BaseModel):
    setup: str = Field(description = "这个笑话的开头")
    punchline : str = Field(description = "这个笑话的妙语")
    rating: Optional[int] = Field(default=None,description = "从1-10分，给这个笑话评分")

class Data(BaseModel):
    jokes: List[Joke]

model_with_structured = model.with_structured_output(Data)
print(model_with_structured.invoke("分别讲一个唱歌和跳舞的笑话"))

