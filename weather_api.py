import requests

# API Documentation: https://openweathermap.org/api

API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "973d94ecc2eb26776ae8bf6100d58f0a"

prefix = "Weather in "

initial_text = "Weather:"
invalid_syntax_message = "Invalid Request. Check syntax and try again!"

def find_location(text):
    '''
    Returns the location from a SMS request
    :param text: Input text to retrieve location from
    :return: location for requested weather data
    '''
    index = text.find(prefix)

    if index < 0:
        return None

    location = text[len(prefix):]

    return location

def retrieve_request_url(location):
    '''
    Retireves the request url for the Open Weather Map Api given the city location
    :param location: The location to retrieve weather data from
    :return: url: The Open Weather Map Api request url
    '''
    url = API_ENDPOINT + "q=" + location + "&" + "appid=" + API_KEY
    return url

def convertTemperature(text):
    kelvin = float(text)
    farenheit = round(kelvin*(9/5) - 459.67, 2)
    celsius = round(kelvin - 273.15, 2)

    return str(farenheit), str(celsius)

def get_weather(text):
    '''
    Makes a Open Weather Map Api call given a text message
    :param text: message in the form ' Weather at location'
    :return: text: overall weather data for location
    '''
    location = find_location(text)
    if location is None:
        return invalid_syntax_message

    url = retrieve_request_url(location)
    response = requests.get(url)
    json = response.json()

    response_code = int(json['cod'])

    if response_code != 200:
        return invalid_syntax_message

    response = format_response(json)

    return response


def format_response(json):
    '''
    Formats the response from an Open Weather Map API call for the SMS response
    :param json: the json response from the API call
    :return: text: the message to be sent to the user
    '''
    result = []
    result.append(initial_text)

    result.append('Description: ' + str(json['weather'][0]['main']) + ' - ' + str(json['weather'][0]['description']))
    temp_farenheit, temp_celsius = convertTemperature(json['main']['temp'])

    result.append('Temperature: ')
    result.append(str(temp_farenheit + ' F'))
    result.append(str(temp_celsius + ' C'))

    result.append('Humiditiy: ' + str(json['main']['humidity']))
    result.append('Wind Speed: ' + str(json['wind']['speed']))

    response = "\n".join(result)

    return response
