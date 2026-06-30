from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage


#LangChain初始化模型的基本用法
# deepseek_model = init_chat_model(model="deepseek-chat",model_provider= "deepseek")
# res = deepseek_model.invoke(["你是谁"]).content
# print(res)


# # 定义可配置的模型（模型模拟器）
# config_model = init_chat_model(temperature=0.7)
# messages = [
#     SystemMessage(content="请帮我补全一段故事，100字以内"),
#     HumanMessage(content="一只闫路甲正在干什么")
# ]
#
# print(config_model.invoke(input = messages, config={"configurable" : {"model" : "deepseek-chat"}}).content)


# 可配置的模型(默认参数)  修改参数
model = init_chat_model(
    model= "deepseek-chat",
    model_provider="deepseek",
    temperature = 0.3,
    max_tokens = 1024,
    # 注意一定要在"max_tokens"后面加个 ,
    configurable_fields=("max_tokens",),
    config_prefix = "first"
)


messages = [
    SystemMessage(content="请帮我补全一段故事，100字以内"),
    HumanMessage(content="一只闫路甲正在干什么")
]


result = model.invoke(
    input = messages,
    config={
        "configurable" : {
            "first_max_tokens" : 100,
        }
    }
)


print(result.content)



