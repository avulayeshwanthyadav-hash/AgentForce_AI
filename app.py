from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import chatbot

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_bot():

    user_msg = request.form.get("Body")

    print("Incoming message:", user_msg)

    reply = chatbot(user_msg)

    print("Reply:", reply)

    response = MessagingResponse()
    msg = response.message()
    msg.body(reply)

    return str(response)

@app.route("/")
def home():
    return "Server Running"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
