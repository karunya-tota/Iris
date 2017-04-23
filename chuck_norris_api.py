import requests

def get_jokes():
    '''
    Makes a Chuck Norris API call to get a joke
    :return: a random joke about Chuck Norris
    '''
    url = "http://api.icndb.com/jokes/random"

    response = requests.get(url)
    if response.status_code == 404 or response.status_code == 500:
        return None
    json = response.json()

    result = None
    if "value" in json:
        value = json["value"]
        if "joke" in value:
            result = value["joke"]

    return str(result)
