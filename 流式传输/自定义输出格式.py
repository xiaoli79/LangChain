from typing import Iterable, List

from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model= "gpt-4o-mini")

parser = StrOutputParser()

# 自定义输出生成器
def split_into_list(input: Iterable[str]) -> Iterable[List[str]]:
    buffer = ""
    for chunk in input:
        buffer += chunk
        while("。" in buffer):
            stop_index = buffer.index("。")
            yield [buffer[:stop_index].strip()]
            buffer = buffer[stop_index+1:]
    yield[buffer.strip()]

# 链条
chain = model | parser | split_into_list

for chunk in chain.stream("写一段关于爱情的歌词，需要5句话，每句话用中文句号隔开."):
    print(chunk,end="|",flush=True)


