from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()
chat_history = []
chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful conversational agent.'),
    ('human', '{question}'),
    MessagesPlaceholder(variable_name="chat_history")
])
with open("chat_history.txt", "r") as file:
    chat_history = file.readlines()

model = chat_template.invoke({
    "question": "What is LangChain?",
    "chat_history": chat_history
})
print(model)