from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
#import os
#from twilio.rest import Client
import dbFunctions

#from dbFunctions import create_server_connection
app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message(request.form["Body"])

    
    connection=dbFunctions.create_server_connection("localhost", "rskuma", "password")


    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

