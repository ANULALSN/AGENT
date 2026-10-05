from openai import OpenAI
import os
from dotenv import load_dotenv
from groq import Groq
#load environmental variables
load_dotenv()

#Create an instance of the openAPI class

openai_client=Groq(api_key=os.getenv("OPENAI_API_KEY"))

def generate_text_basic(prompt: str, model = "openai/gpt-oss-120b", system_prompt: str = "You are a helpful AI assistant."):
    response = openai_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
            ]
        )
    
    return response.choices[0].message.content
# models = openai_client.models.list()
# print("Available Models:")
# for m in models.data:
#     print("-", m.id)

def generate_text_with_conversation(messages,model = "openai/gpt-oss-120b"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=messages
        )
    return response.choices[0].message.content