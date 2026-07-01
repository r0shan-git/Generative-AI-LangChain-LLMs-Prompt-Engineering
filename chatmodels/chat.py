# from dotenv import load_dotenv

# load_dotenv()

# from langchain.chat_models import init_chat_model

# model = init_chat_model('gpt-4.1')

# # print(model)

# response = model.invoke("what is ipl cricket?")
# print(response)

# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# model = ChatGroq(
#     model="llama-3.3-70b-versatile"
# )

# response = model.invoke("What is IPL cricket 2026?")

# print(response.content)

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2506",temperature=0.7,max_tokens=20,
)

response = model.invoke("how to introduce in interview?")

print(response.content)