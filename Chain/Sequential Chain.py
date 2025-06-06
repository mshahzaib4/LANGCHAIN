from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
Prompt1 = PromptTemplate(
    template = "Generate a detail report on {topic}",
    input_variables= ["topic"]
) 
Prompt2 = PromptTemplate(
    template = "Generate a 1 line report summary {topic}",
    input_variables= ["topic"]
) 
model = OpenAI()

parser = StrOutputParser()
chain = Prompt1 | model | parser | Prompt2 | model | parser
print(chain.invoke({"topic":"cricket"})) 
chain.get_graph().print_ascii()