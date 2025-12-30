import os
from typing import List
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader,
    UnstructuredPowerPointLoader,
    UnstructuredMarkdownLoader
)
from langchain.schema import Document

class DocumentLoader:
    @staticmethod
    def load_document(file_path: str) -> List[Document]:
        ext = os.path.splitext(file_path)[-1].lower()
        if ext == ".pdf":
            loader = PyPDFLoader(file_path)
        elif ext == ".docx":
            loader = Docx2txtLoader(file_path)
        elif ext == ".txt":
            loader = TextLoader(file_path)
        elif ext == ".csv":
            loader = CSVLoader(file_path)
        elif ext == ".pptx":
            loader = UnstructuredPowerPointLoader(file_path)
        elif ext == ".md":
            loader = UnstructuredMarkdownLoader(file_path)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")
        
        return loader.load()

    @staticmethod
    def load_multiple(file_paths: List[str]) -> List[Document]:
        all_docs = []
        for path in file_paths:
            all_docs.extend(DocumentLoader.load_document(path))
        return all_docs
