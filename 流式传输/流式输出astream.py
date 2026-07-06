import asyncio

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model= "gpt-4o-mini")

async def async_stream():
    print("------异步调用--------")
    async for chunk in model.astream("写一段关于秋天的作文，1000字"):
        print(chunk.content,end="|",flush=True)


asyncio.run(async_stream())
