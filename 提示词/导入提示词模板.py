# Create a LangSmith API in Settings > API Keys
# Make sure API key env var is set:
# import os; os.environ["LANGSMITH_API_KEY"] = "<your-api-key>"
from langchain_openai import ChatOpenAI
from langsmith import Client

client = Client()
prompt = client.pull_prompt("hardkothari/prompt-maker", dangerously_pull_public_prompt=True)

model = ChatOpenAI(model = "gpt-4o-mini")
chain = prompt | model

while True:
    task = input("\n你的任务是什么(输入quit退出聊天)")
    if task == "quit":
        break
    lazy_prompt = input("\n你当前任务对应的提示词是什么? (输入quit退出聊天)")
    chain.invoke({"task":task,"lazy_prompt":lazy_prompt}).pretty_print()



