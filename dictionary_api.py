import requests

APP_ID = '86a84c22'
APP_KEY = 'd310496f693eabcc2e909bdede2a217e'

invalid_syntax_message = "Invalid Request. Check syntax and try again!"
language = "en"

valid_commands = ["pronounce", "define"]

def process_text(text):
    '''
    Separate the query into a command and the corresponding word
    :param text: the query text entered by the user
    :return: the command and the word
    '''
    text = text.split()

    if len(text) != 2:
        return invalid_syntax_message, invalid_syntax_message

    command = text[0].lower()
    word = text[1].lower()
    return command, word

def process_definition(word, json):
    '''
    Process the sense and subsense definitions of the given word from the json
    :param word: the word to find definitions for
    :param json: the json to extract definitions from
    :return: the text containing all definitions
    '''
    lexical_entries = json["results"][0]["lexicalEntries"]
    entries = lexical_entries[0]["entries"]
    senses = entries[0]["senses"]
    definitions = senses[0]["definitions"]

    if "subsenses" in senses[0]:
        subsenses = senses[0]["subsenses"]
        for subsense in subsenses:
            definitions.append(subsense["definitions"][0])

    definitions = "\n".join(definitions)

    text = ["Spelling: " + word,
            "Definitions: " + definitions]
    text = "\n".join(text)

    return text

def process_pronunciation(word, json):
    '''
    Process the pronunciation, audio file link, and phonetic spelling of the given word from the json
    :param word: the word to find pronunciation for
    :param json: the json to extract pronunciations from
    :return: the text containing pronunciation
    '''
    lexical_entries = json["results"][0]["lexicalEntries"]
    pronunciations = lexical_entries[0]["pronunciations"][0]
    audio_file = pronunciations["audioFile"]
    phonetic_spelling = pronunciations["phoneticSpelling"]

    text = ["Spelling: " + word,
            "Phonetic Spelling: " + phonetic_spelling,
            "Audio File Link: " + audio_file]
    text = "\n".join(text)

    return text

def get_definition(text):
    '''
    Makes an Oxford Dictionary API call given a text message
    :param text: the text containing the command and the word
    :return: the definition or pronunciation if valid word, invalid message otherwise
    '''
    command, word = process_text(text)

    if command is invalid_syntax_message or word is invalid_syntax_message:
        return invalid_syntax_message
    if command not in valid_commands:
        return invalid_syntax_message

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word

    response = requests.get(url, headers={'app_id': APP_ID, 'app_key': APP_KEY})
    if response.status_code == 404 or response.status_code == 500:
        return invalid_syntax_message

    json = response.json()

    if command == "pronounce":
        return process_pronunciation(word, json)
    elif command == "define":
        return process_definition(word, json)
    else:
        return invalid_syntax_message
