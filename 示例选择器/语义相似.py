import os
from langchain_chroma import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# 1. 导入智谱的嵌入模型组件
from langchain_community.embeddings import ZhipuAIEmbeddings

examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]

# 2. 初始化智谱嵌入模型
# 显式指定从你已经配好的 OPENAI_API_KEY 中读取密钥，使用智谱最新的 embedding-3 模型
embeddings = ZhipuAIEmbeddings(
    model="embedding-3"
)

example_prompt = PromptTemplate.from_template("Input:{input}\nOutPut:{output}")

# 3. 这里的逻辑保持不变，Chroma 数据库会调用智谱的 API 来对示例进行向量化存储
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,                # 示例集
    embeddings,              # 使用智谱嵌入模型度量语义相似度
    Chroma,                  # 存储向量，向量数据库
    k=2,                     # 生成示例的数量
)

few_shot_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = example_prompt,
    prefix = "给出每个输出的反义词:",  #前缀
    suffix="Input: {adjective}\nOutput:", #后缀
    input_variables = ["adjective"], #声明变量
)

# 4. 运行并打印最终拼接好的提示词
print(few_shot_prompt.invoke({"adjective": "worried"}).to_messages()[0].content)