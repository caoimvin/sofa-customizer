from flask import Flask, render_template, request, jsonify

from flask_cors import CORS
from difflib import SequenceMatcher
import random

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/customizer")
def customizer():
    return render_template("customizer.html")

@app.route("/api/v1/chat-bot", methods=['GET'])
def chat_bot():
    if 'input' in request.args:
        input_text = request.args['input']

        def similar(a, b):
            return SequenceMatcher(None, a, b).ratio()

        input_text = input_text.lower().split(" ")
        alternative_responses = ["How are you ?", "How can I help you?", "This Dashboard was created with Vue", "I communicate with a Flask (Python) API"]

        for word in input_text:
            if similar(word, "hello") >= 0.7:
                output = "Hello I am the customer service chatbot of this Dashboard"
            elif similar(word, "bye") >= 0.7:
                output = "Have a nice day!"
            else:
                output = random.choice(alternative_responses)
    else:
        return "Error: No input field provided. Please specify an input."
    # results = {}
    # results = "hello my friend"
    return jsonify(output)

if __name__ == '__main__':
    app.run()
