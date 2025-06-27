from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template= "Generate {topic} post Caption for Linkedin post",
    input_variables= ["topic"]
)

prompt2 = PromptTemplate(
    template= "Generate {topic} post Caption for Tweeter post",
    input_variables= ["topic"]
)

parser = StrOutputParser()

runnableParallel = RunnableParallel({
    'tweet': prompt1 | model | parser,
    'linkedin': prompt2 | model | parser
})
print(runnableParallel.invoke({"topic":"AI"}))