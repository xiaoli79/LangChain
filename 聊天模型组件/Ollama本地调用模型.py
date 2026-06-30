from langchain_ollama import ChatOllama

model =ChatOllama(model="deepseek-r1:8b",base_url="http://127.0.0.1:11434")

print(model.invoke("你是谁").content)