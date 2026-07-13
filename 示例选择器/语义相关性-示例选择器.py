from langchain_chroma import Chroma
from langchain_core.example_selectors import MaxMarginalRelevanceExampleSelector
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_zhipu import ZhipuAIEmbeddings

examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]

embeddings = ZhipuAIEmbeddings(
    model="embedding-3"
)


example_prompt = PromptTemplate.from_template("Input:{input}\nOutPut:{output}")

example_selector = MaxMarginalRelevanceExampleSelector.from_examples(
    examples,                # 示例集
    embeddings,              # 使用智谱嵌入模型度量语义相似度
    Chroma,                  # 存储向量，向量存储
    k=4,                     # 生成示例的数量
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