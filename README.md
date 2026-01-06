# Custom RAG Chatbot: End-to-End Solution

## 🎯 Core Objective

This project delivers a scalable, accurate, and fast Retrieval-Augmented Generation (RAG) chatbot designed to handle large documents across multiple file formats. It features a modern, professional Streamlit UI and a modular, deployment-ready backend.

## 🧠 Architecture Overview

The system is built on a modular architecture to ensure scalability and maintainability.

### Textual Architecture Diagram

\`\`\`mermaid
graph TD
    A[User Interface: Streamlit] --> B(File Upload & Chat Input);
    B --> C{Backend API};
    C --> D[Document Loader];
    D --> E[Chunking Manager];
    E --> F[Embedding Manager];
    F --> G[Vector Store: FAISS/Chroma];
    C --> H[RAG Pipeline];
    H --> G;
    H --> I[LLM Manager: OpenAI/HuggingFace];
    I --> J(Answer Generation);
    J --> B;
    G --> K[Persistent Storage];
\`\`\`

### Key Components

| Component | Technology/Module | Purpose |
| :--- | :--- | :--- |
| **Frontend** | Streamlit (`ui/app.py`) | Modern, interactive UI for file upload and chat. |
| **Document Loading** | LangChain Loaders (`backend/loaders`) | Handles PDF, DOCX, TXT, CSV, PPTX, and Markdown. |
| **Chunking** | RecursiveCharacterTextSplitter (`backend/chunking`) | Splits large documents into manageable, overlapping chunks. |
| **Embeddings** | HuggingFace/OpenAI Embeddings (`backend/embeddings`) | Converts text chunks into vector representations. |
| **Vector Store** | FAISS (`backend/vectorstore`) | Stores and enables fast retrieval of document vectors. |
| **LLM** | OpenAI/HuggingFace (`backend/llm`) | Manages the language model for context-aware response generation. |
| **RAG Chain** | ConversationalRetrievalChain (`backend/retriever`) | Orchestrates the retrieval and generation process with chat history. |

## ⚙️ Setup and Installation

For a detailed, step-by-step guide on API keys, system environment variables, and Docker, please refer to the **[SETUP_GUIDE.md](./SETUP_GUIDE.md)**. For quick execution steps, see **[EXECUTION_STEPS.md](./EXECUTION_STEPS.md)**.

### Quick Start (Local)

1.  **Clone the Repository:**
    \`\`\`bash
    git clone https://github.com/gujjala-pranay/custom-rag-chatbot.git
    cd custom-rag-chatbot
    \`\`\`

2.  **Configure Environment:**
    Create a `.env` file with your `OPENAI_API_KEY` and `HUGGINGFACEHUB_API_TOKEN`.

3.  **Run with Docker (Recommended):**
    \`\`\`bash
    docker-compose up --build
    \`\`\`

4.  **Run Manually:**
    \`\`\`bash
    pip install -r requirements.txt
    streamlit run ui/app.py
    \`\`\`

The application will open in your web browser, typically at `http://localhost:8501`.

## 💬 How to Use the Chatbot

1.  **Upload Documents:** Use the file uploader in the sidebar to select one or more documents (PDF, DOCX, TXT, CSV, PPTX, MD).
2.  **Process & Index:** Click the **"Process & Index"** button. The system will load, chunk, embed, and store the documents in the vector database.
3.  **Chat:** Once processing is complete, use the chat input box to ask questions about the content of your uploaded documents.
4.  **View Sources:** The assistant's response will include an expandable **"Sources"** section citing the document names and page numbers used to formulate the answer.

## ☁️ Deployment Guide

The application is designed for easy deployment on various platforms.

### Hugging Face Spaces / Streamlit Cloud

The `app.py` file in the `ui/` directory is the main entry point.

1.  **File Structure:** Ensure your repository structure matches the project structure.
2.  **Dependencies:** The `requirements.txt` file lists all necessary Python packages.
3.  **Secrets:** Configure your `OPENAI_API_KEY` or `HUGGINGFACEHUB_API_TOKEN` as secrets in the deployment platform's settings.

### AWS/GCP/Azure (Basic Guide)

The application can be containerized using Docker for deployment on cloud services.

1.  **Dockerize:** Create a `Dockerfile` to build the application environment.
2.  **Deployment:** Deploy the container to a service like AWS ECS, Google Cloud Run, or Azure Container Instances.
3.  **Volume:** For persistent storage of the FAISS index, configure a persistent volume mount for the `faiss_index` directory.

## 🌟 Resume-Ready Project Description

**End-to-End RAG Chatbot with Large Document Processing**

Developed a production-ready, modular Retrieval-Augmented Generation (RAG) system using LangChain, HuggingFace Embeddings, and Streamlit, capable of processing and querying large documents (100s-1000s of pages) across six file formats (PDF, DOCX, TXT, CSV, PPTX, MD). The solution features a professional, startup-grade UI, persistent FAISS vector storage, and a robust backend with support for both open-source (Mistral/LLaMA) and commercial (OpenAI) LLMs, ensuring high accuracy, context-aware answers with source citations, and seamless cloud deployment.
