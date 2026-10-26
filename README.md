# LangChain-based LLM Chatbot

A lightweight Q&A chatbot powered by **Groq's blazing-fast inference API**, built with **LangChain** and **Streamlit**. Choose from multiple state-of-the-art models, tune temperature and token limits on the fly, and get instant responses — all from a clean browser interface.

**Live Demo:** [llm-import.onrender.com](https://llm-import.onrender.com/)

---

## Features

- **Multiple Model Support** — Switch between Llama 3, Qwen, and GPT-OSS models directly from the sidebar
- **Adjustable Parameters** — Fine-tune `temperature` (0.0–2.0) and `max_tokens` (50–1500) per request
- **LangSmith Tracing** — Optional trace logging via LangSmith for observability and debugging
- **Simple UI** — Clean Streamlit interface, no frontend knowledge required
- **Easy Deployment** — Runs locally or deploys to Render, Railway, or any Python-friendly host

---

## Available Models

| Model | Provider | Best For |
|---|---|---|
| `llama-3.3-70b-versatile` | Meta / Groq | General-purpose, high quality |
| `llama-3.1-8b-instant` | Meta / Groq | Fast, lightweight tasks |
| `openai/gpt-oss-120b` | OpenAI OSS / Groq | Complex reasoning |
| `openai/gpt-oss-20b` | OpenAI OSS / Groq | Balanced speed & quality |
| `qwen/qwen3.6-27b` | Alibaba / Groq | Multilingual & coding tasks |

---

## Tech Stack

- **[LangChain](https://www.langchain.com/)** — Prompt templates, chains, and output parsers
- **[Groq](https://groq.com/)** — Ultra-fast LLM inference backend
- **[Streamlit](https://streamlit.io/)** — Web UI framework
- **[LangSmith](https://smith.langchain.com/)** — Tracing & observability (optional)
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — Environment variable management

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/IoNiCx1/Langchain-based-LLM.git
cd Langchain-based-LLM
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here

# Optional — for LangSmith tracing
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=your_project_name
```

> **Get a free Groq API key** at [console.groq.com](https://console.groq.com)
> **Get a LangSmith key** at [smith.langchain.com](https://smith.langchain.com) (optional)

### 4. Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## Project Structure

```
Langchain-based-LLM/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # API keys (create this yourself, not committed)
├── .gitignore
└── README.md
```

---

## Usage

1. Type your question in the main text input
2. (Optional) Open the **Settings** sidebar to pick a model, adjust temperature, or change max tokens
3. Click **Answer** and wait for the response

**Sidebar controls:**

| Control | Description |
|---|---|
| Model | Which Groq-hosted LLM to use |
| Temperature | Higher = more creative; lower = more deterministic |
| Tokens | Maximum length of the generated response |

---

## Deployment

This app is deployed on **Render**. To deploy your own instance:

1. Push your code to GitHub
2. Create a new **Web Service** on [render.com](https://render.com)
3. Set the build command to `pip install -r requirements.txt`
4. Set the start command to `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
5. Add your environment variables (`GROQ_API_KEY`, etc.) in the Render dashboard

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
