from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
Prompt = PromptTemplate(
    template ='Generate 5 interesting fact about topic {topic}',
    input_variables= ["topic"] )
model = OpenAI()
parser = StrOutputParser()
chain = Prompt | model | parser
result = chain.invoke({"topic":"cricket"})
print(result)
