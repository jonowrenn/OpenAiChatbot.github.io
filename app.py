from openai import OpenAI
import os
import gradio as gr

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

interface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything..."),
    outputs="text",
    title="GPT Chatbot",
    description="A simple chatbot powered by OpenAI GPT-3.5."
)

interface.launch()
