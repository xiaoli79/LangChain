
from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]

example_prompt = PromptTemplate.from_template("Input:{input}\nOutPut:{output}")

example_selectors = LengthBasedExampleSelector(
    examples= examples,
    example_prompt=example_prompt,
    max_length=4,
    # 用于获取字符串长度的函数，用于确定包含哪些示例。
    # 如果没有指定，它是作为默认值提供的。
    # 该函数返回一个整数，表示字符串中由换行符或空格分隔的“单词”数量
    # get_text_length: Callable[[str], int] = lambda x: len(re.split("\n| ", x))
)

few_shot_prompt = FewShotPromptTemplate(
    example_selector = example_selectors,
    example_prompt = example_prompt,
    prefix = "给出每个输出的反义词:",  #前缀,放在所有示例前面,说明任务
    suffix="Input: {adjective}\nOutput:", #后缀,放在所有示例后面,是真正要提问的内容,{adjective}是待填入的变量
    input_variables = ["adjective"], #声明suffix里有哪些变量,invoke时必须传入
)

print(few_shot_prompt.invoke({"adjective": "big"}).to_messages()[0].content)