# 🛠️ Comprehensive Setup Guide

This guide provides step-by-step instructions on how to configure API keys, set up environment variables on your system, and run the project using Docker.

---

## 1. 🔑 Obtaining API Keys

### OpenAI API Key
1.  Go to the [OpenAI Platform](https://platform.openai.com/).
2.  Sign in or create an account.
3.  Navigate to **API Keys** in the sidebar.
4.  Click **"Create new secret key"**, copy it, and save it securely.

### Hugging Face Token
1.  Go to [Hugging Face](https://huggingface.co/).
2.  Sign in and go to **Settings** -> **Access Tokens**.
3.  Click **"New token"**, select **"Read"** role, and copy the token.

---

## 2. 🌍 Setting Up Environment Variables

You have two ways to set these up: using a `.env` file (recommended) or system-wide environment variables.

### Method A: Using `.env` File (Recommended)
1.  In the project root directory, create a file named `.env`.
2.  Add your keys in the following format:
    ```ini
    OPENAI_API_KEY=sk-your-openai-key-here
    HUGGINGFACEHUB_API_TOKEN=hf_your-huggingface-token-here
    ```
3.  The application will automatically load these using the `python-dotenv` library.

### Method B: System Environment Variables

#### **Windows**
1.  Search for **"Edit the system environment variables"** in the Start menu.
2.  Click **Environment Variables**.
3.  Under **User variables**, click **New**.
4.  Variable name: `OPENAI_API_KEY`, Variable value: `your-key`.
5.  Repeat for `HUGGINGFACEHUB_API_TOKEN`.
6.  **Restart your terminal/IDE** for changes to take effect.

#### **macOS / Linux**
1.  Open your terminal.
2.  Edit your shell profile (e.g., `~/.bashrc`, `~/.zshrc`):
    ```bash
    nano ~/.zshrc
    ```
3.  Add the following lines at the end:
    ```bash
    export OPENAI_API_KEY='your-openai-key'
    export HUGGINGFACEHUB_API_TOKEN='your-huggingface-token'
    ```
4.  Save and exit, then run `source ~/.zshrc`.

---

## 3. 🐳 Docker Implementation

Docker is the best way to avoid compatibility issues across different operating systems.

### Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/macOS) or Docker Engine (Linux).

### Running the Project
1.  **Prepare your `.env` file** in the project root as described in Method A.
2.  **Build and Start the Container:**
    ```bash
    docker-compose up --build
    ```
3.  **Access the App:**
    Open your browser and go to `http://localhost:8501`.

### Why use Docker?
- **Isolation:** No need to install Python or libraries on your host system.
- **Consistency:** The app runs in the exact same environment (Debian-based) regardless of your OS.
- **Persistence:** Your uploaded data and vector indexes are saved in the `./data` and `./faiss_index` folders on your host machine via Docker volumes.

---

## 4. 🧪 Troubleshooting
- **Quota Errors:** If you see "Quota exceeded", the system will automatically try the other provider if you have both keys configured.
- **Docker Issues:** Ensure Docker is running before executing `docker-compose`. If a port is already in use, change the port mapping in `docker-compose.yml`.
