from langchain_openai import ChatOpenAI

model = ChatOpenAI(model= "gpt-4o-mini")


# JSON Schema
jsdn_schema = {
    "title": "joke",
    "description": "给用户讲一个笑话。",
    "type": "object",
    "properties": {
        "setup": {
            "type": "string",
            "description": "这个笑话的开头"
        },
        "punchline": {
            "type": "string",
            "description": "这个笑话的妙语"
        },
        "rating": {
            "type": "integer",
            "description": "从1到10分，给这个笑话评分",
            "default": None
        }
    },
    "required": ["setup", "punchline"]
}



model_with_structured = model.with_structured_output(jsdn_schema)
print(model_with_structured.invoke("分别讲一个唱歌和跳舞的笑话"))
