from langchain_community.example_selectors import NGramOverlapExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_zhipu import ZhipuAIEmbeddings

# 翻译示例
examples = [
    {"input": "See Spot run.", "output": "看见Spot跑。"},
    {"input": "My dog barks.", "output": "我的狗叫。"},
    {"input": "Spot can run.", "output": "Spot可以跑。"},
]

example_prompt = PromptTemplate.from_template("Input:{input}\nOutPut:{output}")

embeddings = ZhipuAIEmbeddings(
    model="embedding-3"
)

# 示例选择器(NGram)
Ngram = NGramOverlapExampleSelector(
    examples= examples,
    example_prompt= example_prompt,
    threshold= -1.0   # 阈值
                     # 负值代表不相干的示例也会被筛选出来
                     # 0.0  输出结果是只与输入重叠的示例
                     # 大于1.0 排除所有示例， 返回空列表
)


few_shot_prompt = FewShotPromptTemplate(
    example_selector = Ngram,
    example_prompt = example_prompt,
    prefix = "给出每个输入的中文翻译:",  #前缀
    suffix="Input: {sentence}\nOutput:", #后缀
    input_variables = ["sentence"], #声明变量
)

print(few_shot_prompt.invoke({"sentence": "Spot can run fast"}).to_messages()[0].content)
