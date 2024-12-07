import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user",  "content": prompt}]
    )
        
    return response.choices[0].message["content"].strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit" , "exit"]:
            break 

        response = chat_with_gpt(user_input)
        print(f"AI: {response}")
