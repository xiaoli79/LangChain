from langchain_chroma import Chroma
from langchain_core.example_selectors import LengthBasedExampleSelector, SemanticSimilarityExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import OpenAIEmbeddings

examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]

example_prompt = PromptTemplate.from_template("Input:{input}\nOutPut:{output}")

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,   # 示例集
    OpenAIEmbeddings(model="text-embedding-3-Large"),  #使用嵌入模型的能力度量语义
    Chroma,  # 存储向量，向量数据库
    k=2,  # 生成示例的数量
)

few_shot_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = example_prompt,
    prefix = "给出每个输出的反义词:",  #前缀,放在所有示例前面,说明任务
    suffix="Input: {adjective}\nOutput:", #后缀,放在所有示例后面,是真正要提问的内容,{adjective}是待填入的变量
    input_variables = ["adjective"], #声明suffix里有哪些变量,invoke时必须传入
)

print(few_shot_prompt.invoke({"adjective": "worried"}).to_messages()[0].content)