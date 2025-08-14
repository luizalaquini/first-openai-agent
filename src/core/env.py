import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

API_KEY_OPENAI = os.getenv('API_KEY_OPENAI')
PROJECT_OPENAI = os.getenv('PROJECT_OPENAI')
