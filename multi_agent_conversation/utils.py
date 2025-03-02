import os
from dotenv import load_dotenv, find_dotenv

# Function to load environment variables from a .env file
def load_env():
    _ = load_dotenv(find_dotenv())

# Function to retrieve the OpenAI API key from environment variables
def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if not openai_api_key:
        raise ValueError("OpenAI API key not found. Make sure it's set in the .env file.")
    
    #print("API Key Loaded:", openai_api_key)
    
    return openai_api_key
