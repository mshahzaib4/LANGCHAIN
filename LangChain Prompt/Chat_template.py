from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful {domain} expert. You will answer the question based on the context provided.'),
    ('human', 'Explain in simple terms What is {question}'),
])
model = ChatOpenAI()
prompt = chat_template.invoke({
    "domain": "AI",
    "question": "What is LangChain?"
})
print(prompt)