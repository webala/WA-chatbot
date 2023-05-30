from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.route('/', methods=['POST'])

def bot():
    user_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    print('user message: ', user_msg)

    msg = response.message('Hey there. This is Mr. Robot chatbot')

if __name__ == "__main__":
    app.run()