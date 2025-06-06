from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object= Feedback)

model = OpenAI()
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "Classify the sentiment of the  following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables= ["feedback"],
    partial_variables= {'format_instruction': parser2.get_format_instructions()}

) 

Prompt2 = PromptTemplate(
    template= "Write an appropriate response to this positive feedback. \n{feedback}"
)

Prompt2 = PromptTemplate(
    template= "Write an appropriate response to this negative feedback. \n{feedback}"
)

classification_chain = prompt1 | model | parser2
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive", Prompt2 | model | parser),
    (lambda x:x.sentiment == "negative", Prompt2 | model | parser),
    RunnableLambda(lambda x: "Sentiment are not find")
     
)

chain = classification_chain|branch_chain
print(chain.invoke({"feedback": "This is a beautiful phone"}))