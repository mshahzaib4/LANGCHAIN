from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage( 
               content="You are a helpful assistant that provides information about various topics.")
]
chat_history = []
model = ChatOpenAI()
while True:
    user_input = input("You: ")
    messages.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    response = model.invoke(messages)
    chat_history.append(AIMessage(content=response.content))
messages.append(AIMessage(content=response.content))
print("AI:", response.content)