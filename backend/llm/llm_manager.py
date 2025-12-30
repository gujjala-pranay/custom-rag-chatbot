import os
from langchain_openai import ChatOpenAI
from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv

load_dotenv()

class LLMManager:
    def __init__(self, provider: str = "openai", model_name: str = "gpt-4o-mini"):
        self.provider = provider
        self.model_name = model_name

    def get_llm(self):
        if self.provider == "openai":
            return ChatOpenAI(model=self.model_name, temperature=0)
        elif self.provider == "huggingface":
            # Requires HUGGINGFACEHUB_API_TOKEN in .env
            return HuggingFaceHub(
                repo_id=self.model_name,
                model_kwargs={"temperature": 0.1, "max_length": 512}
            )
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")
