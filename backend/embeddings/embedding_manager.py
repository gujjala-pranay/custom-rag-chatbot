import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

class EmbeddingManager:
    def __init__(self, provider: str = "huggingface", model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.provider = provider
        if provider == "openai":
            self.embeddings = OpenAIEmbeddings()
        else:
            self.embeddings = HuggingFaceEmbeddings(model_name=model_name)

    def get_embeddings(self):
        return self.embeddings
