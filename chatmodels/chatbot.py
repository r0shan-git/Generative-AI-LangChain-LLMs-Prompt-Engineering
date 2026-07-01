from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage # add this for better message handling

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

print("choose your AI model ")
print("Press 1 for Angry Mode")
print("Press 2 for Funny Mode")
print("Press 3 for Sad Mode")

mode = input("Enter your choice: ")

if mode == "1":
    message=[SystemMessage(content="You are an angry ai agent")]
elif mode == "2":
    message=[SystemMessage(content="You are a funny ai agent")]
elif mode == "3":
    message=[SystemMessage(content="You are a sad ai agent")]
else:
    print("Invalid choice. Defaulting to Funny Mode.")
    message=[SystemMessage(content="You are a funny ai agent")]

print("----------------------------Welcome! Type 'exit' to exit the application----------------------------")

while True:
    user_input = input("You: ")
    message.append(HumanMessage(content=user_input))
    if user_input == "0":
        break
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("BOT  :",response.content)

print(message)