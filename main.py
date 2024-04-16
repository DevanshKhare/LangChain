import openai
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI()

response = llm.invoke("What is the capital of india?")
print(response.content)
