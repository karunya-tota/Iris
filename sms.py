from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

ACCOUNT_SID = 'AC16f7ed5e9f9cf753e9d63d770f0c74c7'
AUTH_TOKEN = '48609fe0ecfbe5bf3f9d97dc8934c4f8'
FROM_NUMBER = "+13214183889"

# client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_message(number, message_body):
    '''
    Sends a message from the Twilio Account Number to a Twilio Verified Number
    :param number: Number to send a message to
    :param message_body: Text to be sent in message
    :return: message created
    '''
    twilio_account = client.api.account
    message = ''
    try:
        message = twilio_account.messages.create(to=number, from_=FROM_NUMBER, body=message_body)

    except TwilioRestException:
       return 'Unverified Phone Number!'

    return message

def print_messages():
    '''
    Prints the messages that have been sent previously
    :return: prints messages in the client list
    '''
    for message in client.messages.list():
        print(message.body)

def main():
    '''
    Asks User for input number to send text message
    :return:
    '''
    number = input('What number would you like to text?')
    text = input('Please enter the message you would like to send:')
    message = send_message(number, text)
    print('Sent Message: ' + message.body)
    print('Status: ' + message.status)
    print('To: ' + message.to)
    print('From: ' + message.from_)

if __name__ == "__main__":
    main()
