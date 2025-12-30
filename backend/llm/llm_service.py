import os
from typing import Optional, Any
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

class LLMService:
    """
    Service to manage and switch between different LLM providers.
    Supports OpenAI and Open-Source models like LLaMA-3 via HuggingFace.
    """
    
    def __init__(self, provider: str = "openai", model_name: Optional[str] = None, temperature: float = 0.1):
        self.provider = provider.lower()
        self.temperature = temperature
        
        if self.provider == "openai":
            self.model_name = model_name or "gpt-4o-mini"
            self.llm = self._init_openai()
        elif self.provider == "llama3" or self.provider == "huggingface":
            # Default to LLaMA-3-8B-Instruct if no model name is provided
            self.model_name = model_name or "meta-llama/Meta-Llama-3-8B-Instruct"
            self.llm = self._init_huggingface()
        else:
            raise ValueError(f"Unsupported provider: {self.provider}. Choose 'openai' or 'llama3'.")

    def _init_openai(self) -> ChatOpenAI:
        """Initialize OpenAI Chat model."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")
        
        return ChatOpenAI(
            model=self.model_name,
            temperature=self.temperature,
            streaming=True
        )

    def _init_huggingface(self) -> HuggingFaceEndpoint:
        """Initialize HuggingFace Endpoint for models like LLaMA-3."""
        hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if not hf_token:
            raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment variables.")
        
        return HuggingFaceEndpoint(
            repo_id=self.model_name,
            huggingfacehub_api_token=hf_token,
            temperature=self.temperature,
            max_new_tokens=1024,
            top_k=10,
            top_p=0.95,
            typical_p=0.95,
            repetition_penalty=1.03,
        )

    def get_llm(self) -> Any:
        """Return the initialized LLM instance."""
        return self.llm

    @classmethod
    def list_supported_providers(cls):
        """List the currently supported LLM providers."""
        return ["openai", "llama3", "huggingface"]

# Example Usage:
# service = LLMService(provider="llama3")
# llm = service.get_llm()
