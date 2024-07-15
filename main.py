from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No OPENAI_API_KEY found in environment variables.")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

app = Flask(__name__, static_url_path='', static_folder='static')

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/chat", methods=["POST"])
def chat():
    try:
        prompt = request.form.get("prompt")
        file = request.files.get("file")
        logging.debug(f"Received prompt: {prompt}")
        if file:
            logging.debug(f"Received file: {file.filename}")

        if not prompt and not file:
            raise ValueError("No prompt or file provided.")

        # For demonstration purposes, let's assume we only process the prompt
        response_text = ""
        if prompt:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            logging.debug(f"OpenAI response: {response}")
            response_text = response.choices[0].message.content

        # Here you could add logic to handle the file if needed
        logging.debug(f"Response text: {response_text}")
        
        return jsonify(response_text)
    except Exception as e:
        logging.error(f"Error: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
