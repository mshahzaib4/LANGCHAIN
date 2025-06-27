from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model_name = "GPT-3.5-turbo", temperature = 0.7)

prompt = PromptTemplate(
    input_variables = ["topic"],
    template = "Suggest a Catchy blog little about {topic}."
)
topic = input("Enter a topic : ")
formatted_prompt = prompt.template(topic = topic)
blog_tittle = llm.predict(formatted_prompt)
print(blog_tittle) 