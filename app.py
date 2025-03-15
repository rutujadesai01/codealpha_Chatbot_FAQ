from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# Initialize ChatBot
chatbot = ChatBot("FAQBot", storage_adapter="chatterbot.storage.SQLStorageAdapter", database_uri="sqlite:///faqbot.sqlite3")

# Train the chatbot
trainer = ListTrainer(chatbot)
faq_data = [
    "What are your business hours?",
    "We are open from 9 AM to 6 PM, Monday to Friday.",
    "How can I contact customer support?",
    "You can contact us via email at support@example.com or call +123456789.",
    "What is your return policy?",
    "You can return items within 30 days of purchase with a valid receipt.",
    "Do you offer international shipping?",
    "Yes, we offer international shipping to selected countries."
]
trainer.train(faq_data)

# Home route - renders the chat interface
@app.route("/")
def home():
    return render_template("index.html")

# Chat route - handles user input and chatbot response
@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    bot_response = str(chatbot.get_response(user_message))
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
