# 🧠 Arch Technologies – Local GenAI Chat

A modern, ChatGPT-style AI chat application built with **Streamlit** and powered by a **local LLM via Ollama**.

## 🚀 Features
- ChatGPT-like UI and responses
- Real-time streaming output
- Local LLM backend (privacy-first)
- Clean, modern interface
- Fast response loop

## 🛠 Tech Stack
- Frontend: Streamlit
- Backend: Ollama (Local LLM)
- Model: qwen2.5 (configurable)

## ⚙️ Requirements
- Python 3.9+
- Ollama installed and running
- A local model pulled (e.g. `qwen2.5:0.5b`)

## ▶️ Run Locally
```bash
ollama run qwen2.5:0.5b
streamlit run app.py
