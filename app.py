from flask import Flask, request, jsonify, render_template
from chatbot import process_message
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    response = process_message(message)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
