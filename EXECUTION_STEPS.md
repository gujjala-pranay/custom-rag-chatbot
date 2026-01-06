# 🚀 Execution Steps

Follow these steps to get your Custom RAG Chatbot up and running on your system.

---

## 🛠️ Option 1: Using Docker (Recommended)
This is the easiest way to run the project without worrying about Python versions or library dependencies.

1.  **Open your Terminal or Command Prompt.**
2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/gujjala-pranay/custom-rag-chatbot.git
    cd custom-rag-chatbot
    ```
3.  **Create Environment File:**
    - Create a file named `.env` in the root folder.
    - Add your keys:
      ```ini
      OPENAI_API_KEY=your_key_here
      HUGGINGFACEHUB_API_TOKEN=your_token_here
      ```
4.  **Launch the Application:**
    ```bash
    docker-compose up --build
    ```
5.  **Access the Chatbot:**
    - Open your browser and go to: `http://localhost:8501`

---

## 🐍 Option 2: Manual Local Setup
Use this if you prefer running the code directly on your system.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/gujjala-pranay/custom-rag-chatbot.git
    cd custom-rag-chatbot
    ```
2.  **Create a Virtual Environment (Optional but Recommended):**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set Up Environment Variables:**
    - Create a `.env` file in the root folder (same as step 3 in Option 1).
5.  **Run the Application:**
    ```bash
    streamlit run ui/app.py
    ```
6.  **Access the Chatbot:**
    - The terminal will provide a URL, usually `http://localhost:8501`.

---

## 💬 Using the Chatbot Interface

Once the app is running:
1.  **Sidebar Configuration:**
    - Select your preferred **LLM Provider** (OpenAI or HuggingFace).
    - Select your **Embedding Provider**.
2.  **Upload Documents:**
    - Drag and drop your files (PDF, DOCX, etc.) into the upload area.
    - Click **"Process & Index"**. Wait for the "Success" message.
3.  **Start Chatting:**
    - Type your question in the chat box at the bottom.
    - View the answer and expand the **"Sources"** section to see citations.
4.  **Reset:**
    - Use the **"Clear Chat History"** button in the sidebar to start a fresh conversation.
