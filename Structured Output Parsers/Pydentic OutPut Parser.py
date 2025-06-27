from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv() 
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2b-it",  
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person")
    city: str = Field(description="City where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate(
    template="Give me the name, age, and city of a fictional {place} person \n{format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)    
prompt = template.invoke({'place':"Indian"})
result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(result.content)
print("--------------------------------------------------")
print(final_result)

