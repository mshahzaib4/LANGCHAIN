from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)
prompt2= PromptTemplate(
    template= "Explain thr Following Joke {joke}",
    input_variables = ["joke"]
    )

model = ChatOpenAI()
parser = StrOutputParser()

# Create the chain
chain = prompt | model | parser | prompt2 | model | parser

print(chain.invoke({"topic": "AI"}))