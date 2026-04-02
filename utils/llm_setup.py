import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def get_llm(user_api_key=None):
    api_key = user_api_key if user_api_key else os.getenv("GROQ_API_KEY")

    return ChatGroq(
model="openai/gpt-oss-120b",
api_key=api_key
)