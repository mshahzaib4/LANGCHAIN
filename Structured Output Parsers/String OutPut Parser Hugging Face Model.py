from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2b-it",  
    task="text-generation"
)
model = ChatHuggingFace(llm = llm)

template1 = PromptTemplate(
    template = "Write a detailed report on {topic}"
    , input_variables = ["topic"])

template2 = PromptTemplate(
    template= "Write a 5 line summary of following text.\n{text}"
    , input_variables=["text"]) 

prompt1 = template1.invoke({'topic': 'Artificial Intelligence'})    

chain = template1 | model | template2 | model
result = chain.invoke({'topic': 'Artificial Intelligence'})
print(result.content)