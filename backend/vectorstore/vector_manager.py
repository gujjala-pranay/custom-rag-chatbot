import os
from typing import List
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

class VectorManager:
    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.vector_db = None

    def create_vector_db(self, documents: List[Document], save_path: str = "faiss_index"):
        self.vector_db = FAISS.from_documents(documents, self.embeddings)
        self.vector_db.save_local(save_path)
        return self.vector_db

    def load_vector_db(self, load_path: str = "faiss_index"):
        if os.path.exists(load_path):
            self.vector_db = FAISS.load_local(load_path, self.embeddings, allow_dangerous_deserialization=True)
            return self.vector_db
        return None

    def add_documents(self, documents: List[Document], save_path: str = "faiss_index"):
        if self.vector_db is None:
            self.create_vector_db(documents, save_path)
        else:
            self.vector_db.add_documents(documents)
            self.vector_db.save_local(save_path)
        return self.vector_db
