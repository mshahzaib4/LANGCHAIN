from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

def word_count(text):
    return len(text.split())

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template= "Generate {topic} post Caption for Linkedin post",
    input_variables= ["topic"]
)

parser = StrOutputParser()

joke_chain = prompt1 | model | parser

parallel_runnable = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "word_count": RunnableLambda(word_count)
    }
)

final_chain = joke_chain | parallel_runnable

print(final_chain.invoke({"topic":"AI"}))