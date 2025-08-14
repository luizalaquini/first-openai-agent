import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
API_KEY_OPENAI=os.getenv('API_KEY_OPENAI')
PROJECT_OPENAI=os.getenv('PROJECT_OPENAI')

client = OpenAI (
    api_key=API_KEY_OPENAI,
    project=PROJECT_OPENAI
)

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
