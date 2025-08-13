---
title: GPT Chatbot
emoji: 💬
colorFrom: indigo
colorTo: blue
sdk: gradio
app_file: app.py
pinned: false
---

# GPT Chatbot

A conversational AI chatbot built with **Gradio** and the **OpenAI API**.

**Live demo on Hugging Face Spaces:**  
👉 [https://huggingface.co/spaces/jonowrenn/gpt-chatbot](https://huggingface.co/spaces/jonowrenn/gpt-chatbot)

> ⚠️ Note: This demo runs with a shared API key and a hard usage limit.  
> If the limit is reached, the chatbot will be unavailable until the next billing cycle.  
> To run without limits, clone the repo and use your own OpenAI API key.

---

## Features
- Chat with GPT-3.5 in a clean Gradio interface
- Optional topic guidance for focused conversations
- Remembers recent conversation context
- Deployable on Hugging Face Spaces

## Run Locally
1. Clone the repo:
    git clone https://github.com/jonowrenn/gpt-chatbot
    cd gpt-chatbot

2. Install dependencies:
    pip install -r requirements.txt

3. Create a .env file and add your key:
    OPENAI_API_KEY=your_api_key_here

4. Run the app:
    python app.py

License
MIT License