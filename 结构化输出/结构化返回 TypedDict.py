from typing import Optional, TypedDict,Annotated
from langchain_openai import ChatOpenAI


model = ChatOpenAI(model= "gpt-4o-mini")

class Joke(TypedDict):
    setup: str = Annotated[str,..., "这个笑话的开头"]
    punchline : str = Annotated[str,..., "这个笑话的妙语"]
    rating:  Annotated[Optional[int],None ,"从1-10分，给这个笑话评分"]

# include_raw = True 返回完整的AIMessage 。默认为false
model_with_structured = model.with_structured_output(Joke,include_raw=True)

print(model_with_structured.invoke("讲一个关于跳舞的笑话"))