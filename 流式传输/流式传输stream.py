from langchain_openai import ChatOpenAI

model = ChatOpenAI(model= "gpt-4o-mini")



chunks = []
for chunk in model.stream("写一段关于春天的作文，1000字"):
    # chunk的类型为AIMessage
    chunks.append(chunk)
    print(chunk.content,end="|",flush=True)