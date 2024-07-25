import africastalking
import os
from flask import Flask, request
import AuthCodeGenerator
from config import config


africastalking.initialize(
    username= config.UserName,
    api_key= config.API_Key
)

sms = africastalking.SMS

class send_sms:
    def send(self):
        recipients = ["+254114883285"]
        message = "Hello your Authentication Code is " + AuthCodeGenerator.AuthCode 
        sender = "78980"
        try:
            response = sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print(f'Houston, we have a problem: {e}')

app = Flask(__name__)

@app.route('/incoming', methods=['POST'])
def incoming_sms():
    data = request.form
    print(f"Incoming message: {data}")
    return "Message received", 200

@app.route('/delivery_reports', methods=['POST'])
def delivery_reports():
    data = request.form
    print(f"Delivery report: {data}")
    return "Delivery report received", 200

if __name__ == "__main__":
    sender = send_sms()
    sender.send()
    app.run(debug=True, port=os.environ.get("PORT", 5000))
