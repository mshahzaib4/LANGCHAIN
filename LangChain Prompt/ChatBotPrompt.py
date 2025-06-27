from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
chat_historty = []
while True:
    user_input = input("You: ")
    chat_historty.append(user_input)
    if user_input.lower() == "exit":
        break
    response = model.invoke(chat_historty)
    chat_historty.append(response.content)
    print(f"AI: {response.content}")
