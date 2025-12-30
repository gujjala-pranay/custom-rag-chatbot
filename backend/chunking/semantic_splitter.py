from langchain_experimental.text_splitter import SemanticChunker
from backend.embeddings.embedding_manager import EmbeddingManager

class SemanticChunkManager:
    def __init__(self, embeddings):
        self.splitter = SemanticChunker(embeddings)

    def split_documents(self, documents):
        return self.splitter.split_documents(documents)
