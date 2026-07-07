from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model= "gpt-4o-mini")

# 定义提示词模板,Runnable示例
# 方式1
# PromptTemplate(
#     template="介绍{city}的历史",
#     input_variables=["city"],
# )

# 方式2 : 实例化模板
# prompt_template = PromptTemplate.from_template("将文本从{language_from}翻译为{language_to}")
#
# print(prompt_template.invoke({"language_from": "中文", "language_to": "英文"}))

# 处理聊天消息模板
chat_prompt_template = ChatPromptTemplate(
    [
        ("system","将文本从{language_from}翻译为{language_to}"),
        ("user","{text}")
    ]
)

messages = chat_prompt_template.invoke(
    {
        "language_from": "英文",
        "language_to": "中文",
        "text": "hi,what is your name"
    }
)

model.invoke(messages).pretty_print()

