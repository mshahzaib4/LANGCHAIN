from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema 

from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2b-it",  
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name = "fact_1", description = "fact 1 about the topic"),
    ResponseSchema(name = "fact_2", description = "fact 2 about the topic"),                
    ]
 
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give me the name, age, and city of a fictional Character in JSON format.\n{format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({})
print(result.content)
print("--------------------------------------------------")
print(parser.parse(result.content))