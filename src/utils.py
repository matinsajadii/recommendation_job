import openai
from dotenv import load_dotenv
import os

print(f"DOTENV ----> {load_dotenv()}")


openai.api_key = os.getenv("OPENAI_API_KEY")

#Helper function: get embeddings for a text
def get_embeddings(text):
    if isinstance(text, str):  # Check if text is a string
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input=text.replace("\n", " ")
        )
        embedding = response['data'][0]['embedding']
        return embedding
    else:
        return None 