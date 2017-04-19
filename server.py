from google_maps_api import *
from weather_api import *
from recipes_api import *
from flask import Flask
from flask import request
from flask import render_template
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def send_response():
    '''
    Sends a response to the user when they reply to a message sent from Twilio
    :return: string of response sent to user
    '''
    text = str(request.values.get("Body", None))
    if 'Directions' in text:
        response_body = get_directions(text)
    if 'Weather' in text:
        response_body = get_weather(text)
    if 'Recipe' in text:
        response_body = get_recipe(text)
    response = MessagingResponse().message(response_body)
    result = str(response)
    return result

@app.route("/send_message", methods=['GET'])
def send_message():
    '''
    Renders the front-end view for Send Message View
    :return:
    '''
    result = render_template('message.html')
    return result

if __name__ == "__main__":
    app.run(debug=True)
