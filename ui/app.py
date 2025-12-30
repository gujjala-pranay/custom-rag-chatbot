import os
import sys
import streamlit as st
from dotenv import load_dotenv

# Add parent directory to path to import backend modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.loaders.document_loader import DocumentLoader
from backend.chunking.text_splitter import ChunkManager
from backend.embeddings.embedding_manager import EmbeddingManager
from backend.vectorstore.vector_manager import VectorManager
from backend.llm.llm_manager import LLMManager
from backend.retriever.rag_pipeline import RAGPipeline

load_dotenv()

st.set_page_config(page_title="Custom RAG Chatbot", layout="wide")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

def process_documents(uploaded_files):
    with st.spinner("Processing documents..."):
        temp_dir = "data/temp"
        os.makedirs(temp_dir, exist_ok=True)
        file_paths = []
        for uploaded_file in uploaded_files:
            file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            file_paths.append(file_path)
        
        # Load
        loader = DocumentLoader()
        docs = loader.load_multiple(file_paths)
        
        # Split
        splitter = ChunkManager()
        chunks = splitter.split_documents(docs)
        
        # Embed & Store
        embed_manager = EmbeddingManager(provider=st.session_state.embed_provider)
        vector_manager = VectorManager(embed_manager.get_embeddings())
        st.session_state.vector_db = vector_manager.create_vector_db(chunks)
        
        # Initialize RAG Chain
        llm_manager = LLMManager(provider=st.session_state.llm_provider, model_name=st.session_state.llm_model)
        rag_pipeline = RAGPipeline(llm_manager.get_llm(), st.session_state.vector_db)
        st.session_state.rag_chain = rag_pipeline.get_chain()
        
        st.success("Documents processed and indexed!")

# Sidebar
with st.sidebar:
    st.title("⚙️ Configuration")
    
    st.subheader("Model Settings")
    st.session_state.llm_provider = st.selectbox("LLM Provider", ["openai", "huggingface"])
    st.session_state.llm_model = st.text_input("Model Name", value="gpt-4o-mini" if st.session_state.llm_provider == "openai" else "mistralai/Mistral-7B-Instruct-v0.2")
    
    st.subheader("Embedding Settings")
    st.session_state.embed_provider = st.selectbox("Embedding Provider", ["huggingface", "openai"])
    
    st.subheader("Upload Documents")
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True, type=["pdf", "docx", "txt", "csv", "pptx", "md"])
    if st.button("Process & Index"):
        if uploaded_files:
            process_documents(uploaded_files)
        else:
            st.warning("Please upload files first.")

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        if st.session_state.rag_chain:
            st.session_state.rag_chain.memory.clear()
        st.rerun()

# Main Chat UI
st.title("💬 Custom RAG Chatbot")
st.markdown("---")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sources" in message:
            with st.expander("Sources"):
                for source in message["sources"]:
                    st.write(f"- {source}")

# Chat input
if prompt := st.chat_input("Ask a question about your documents..."):
    if not st.session_state.rag_chain:
        st.error("Please upload and process documents first!")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.rag_chain.invoke({"question": prompt})
                answer = response["answer"]
                sources = list(set([doc.metadata.get("source", "Unknown") for doc in response["source_documents"]]))
                
                st.markdown(answer)
                with st.expander("Sources"):
                    for source in sources:
                        st.write(f"- {os.path.basename(source)}")
                
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": answer,
                    "sources": [os.path.basename(s) for s in sources]
                })
