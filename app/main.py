from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv()  


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.chatbot import RAGChatbot
from app.pdf_processor import extract_pdf_content
from app.call_service import make_call

app = Flask(__name__)

# Load PDF content and initialize chatbot
PDF_PATH = "data/product_info.pdf"
pdf_content = extract_pdf_content(PDF_PATH)
chatbot = RAGChatbot(knowledge_base=pdf_content)

# Store user contact info
user_data = {}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the AI Chatbot API!"})

@app.route('/submit', methods=['POST'])
def submit_contact():
    data = request.json
    user_data['name'] = data.get('name')
    user_data['phone'] = data.get('phone')
    return jsonify({"message": "Contact information saved!"})

@app.route('/ask', methods=['POST'])
def ask_query():
    query = request.json.get('query')
    if not query:
        return jsonify({"error": "No query provided"}), 400
    response = chatbot.get_answer(query)
    return jsonify({"answer": response['answer']})

@app.route('/callback', methods=['POST'])
def callback():
    phone = user_data.get('phone')
    if not phone:
        return jsonify({"error": "No phone number saved"}), 400
    query = "Tell me about the product."  # Example query
    response = chatbot.get_answer(query)
    message = f"Our product offers the following: {response['answer']}"
    call_sid = make_call(phone, message)
    return jsonify({"message": "Call initiated!", "call_sid": call_sid})

if __name__ == '__main__':
    app.run(debug=True)