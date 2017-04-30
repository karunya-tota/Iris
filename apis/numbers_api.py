import requests

SEPARATOR = " "

def get_user_choice(text):
    '''
    Understands the user choice and returns the corresponding API suffix
    :param text: message in the form of 'Numbers <choice>'
    :return: the suffix to be added to the end of url
    '''

    #remove any leading or trailing spaces from the string
    text = text.strip()

    #check the number of words is exactly two
    words = text.split(SEPARATOR)
    if len(words) != 2:
        return None

    valid_choices = ["trivia",
                     "year",
                     "date",
                     "month"]

    choice = words[1].lower()
    if choice in valid_choices:
        return choice
    else:
        return None

def get_numbers(text):
    '''
    Makes a Numbers API call to get a fact depending on the user choices
    :param text: message in the form of 'Numbers <choice>'
    :return: the text message to be sent to the user
    '''

    #process the user choice to get suffix for API
    user_choice = get_user_choice(text)

    if user_choice is None:
        return None

    url = "http://numbersapi.com/random/" + user_choice + "?json"

    response = requests.get(url)
    if response.status_code == 404 or response.status_code == 500:
        return None
    json = response.json()

    if "text" in json:
        text = json["text"]
        return text
    else:
        return None
