import streamlit as st
import requests
import json

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Arch Technologies – Local GenAI Chat",
    page_icon="🧠",
    layout="centered"
)

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:0.5b"

# ---------------- SYSTEM PROMPT ----------------
SYSTEM_PROMPT = """
You are a modern AI assistant similar to ChatGPT or Gemini.

RULES FOR EVERY RESPONSE:
- Be clear, natural, and human-like
- Avoid robotic phrases like "As an AI language model"
- Use clean formatting:
  - Short paragraphs
  - Bullet points where helpful
  - Headings if explaining concepts
- Give simple explanations first, then details
- Use examples when useful
- Do NOT over-explain unless asked
- Sound confident, helpful, and engaging
"""

# ---------------- UI HEADER ----------------
st.title("🧠 Arch Technologies – Local GenAI Chat")
st.caption("Natural, ChatGPT-style responses powered by a local LLM (Ollama)")

# ---------------- SESSION STATE ----------------
if "chat" not in st.session_state:
    st.session_state.chat = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.subheader("⚙️ Settings")
    st.text(f"Model: {MODEL}")
    st.text("Backend: Local Ollama API")

    if st.button("🗑 Reset Conversation"):
        st.session_state.chat = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
        st.rerun()

# ---------------- CHAT HISTORY ----------------
for msg in st.session_state.chat:
    if msg["role"] in ["user", "assistant"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Ask anything — tech, AI, concepts, ideas…")

if user_input:
    # Add user message
    st.session_state.chat.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        payload = {
            "model": MODEL,
            "messages": st.session_state.chat,
            "stream": True
        }

        # STREAM RESPONSE
        with requests.post(OLLAMA_URL, json=payload, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    data = json.loads(line.decode("utf-8"))
                    token = data.get("message", {}).get("content", "")
                    full_response += token
                    response_placeholder.markdown(full_response + "▌")

        response_placeholder.markdown(full_response)

    # Save assistant response
    st.session_state.chat.append({
        "role": "assistant",
        "content": full_response
    })
