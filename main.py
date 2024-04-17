import openai
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("system", "Tell me the currency of countries that I will ask"),
    ("user", "{input}")
])

chain = prompt | llm  

response = chain.invoke({"input": "india"})


print(response.content)

