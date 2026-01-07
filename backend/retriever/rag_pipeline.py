from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate

class RAGPipeline:
    def __init__(self, llm, vector_db):
        self.llm = llm
        self.vector_db = vector_db
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
        
        self.template = """
        You are a professional assistant. Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Keep the answer concise and professional. Always cite the source document and page/chunk if available.

        Context: {context}

        Question: {question}
        Helpful Answer:"""
        
        self.QA_PROMPT = PromptTemplate(
            template=self.template, input_variables=["context", "question"]
        )

    def get_chain(self):
        return ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vector_db.as_retriever(search_kwargs={"k": 5}),
            memory=self.memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": self.QA_PROMPT}
        )
