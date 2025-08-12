import openai
import gradio as gr
import os

# Load your OpenAI API key from the Hugging Face Secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat(user_input):
    try:
        messages = [
            {"role": "system", "content": "You are a helpful and conversational chatbot."},
            {"role": "user", "content": user_input}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message["content"].strip()
    
    except Exception as e:
        return f"Error: {e}"

# Gradio UI
interface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything..."),
    outputs="text",
    title="GPT Chatbot",
    description="A simple chatbot powered by OpenAI GPT-3.5. Enter a prompt and receive a response."
)

interface.launch()
