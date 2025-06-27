from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch
import dotenv
dotenv.load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="Generate detail report on this topic {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following report {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

detail_report = prompt1 | model | parser

runnable_branch = RunnableBranch(
    (lambda x: len(x.split()) > 500, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = detail_report | runnable_branch

print(final_chain.invoke({"topic": "Russia Vs Ukraine"}))