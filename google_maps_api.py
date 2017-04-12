from bs4 import BeautifulSoup
import requests

API_ENDPOINT = "https://maps.googleapis.com/maps/api/directions/json?"
API_KEY = "AIzaSyAEdm8KvM2X7aaa3B70uPYYHdV72cwqykM"

prefix = "Directions from "
separator = " to "

initial_text = "Directions:"
invalid_syntax_message = "Invalid Request. Check syntax and try again!"

def process_text(text):
    '''
    Returns the Start and End locations from a request
    :param text: Input text to retrieve locations from
    :return: Start and End locations
    '''
    places = text.split(prefix, 1)

    if places is None:
        return None, None
    elif len(places) < 2:
        return None, None
    else:
        places = places[1]

    index = places.find(separator)

    if index < 0:
        return None, None

    start = places[:index]
    end = places[index + len(separator):]

    if start == end:
        return None, None

    return start, end

def retrieve_request_url(start, end):
    '''
    Retireves the request url for the Google Maps Api given the start and end points
    :param start: The starting point in the direction search
    :param end: The ending point in the direction search
    :return: url: The Google Maps API call url
    '''
    start = start.split(" ")
    start = "+".join(start)
    end = end.split(" ")
    end = "+".join(end)

    url = API_ENDPOINT + "origin=" + start + "&" + "destination=" + end + "&" + "key=" + API_KEY
    return url

def make_request(text):
    '''
    Makes a Google Maps API call given a text message
    :param text: message in the form ' Directions from A to B'
    :return: text: overall instructions on how to get to point B from point A
    '''
    start, end = process_text(text)
    if start is None or end is None:
        return invalid_syntax_message

    url = retrieve_request_url(start, end)
    # url = 'https://maps.googleapis.com/maps/api/directions/json?origin=Illini+Union&destination=Live+Latitude&key=AIzaSyAEdm8KvM2X7aaa3B70uPYYHdV72cwqykM'

    response = requests.get(url)
    json = response.json()

    if json['routes'] == []:
        return invalid_syntax_message

    routes = json["routes"][0]
    legs = routes["legs"][0]
    steps = legs["steps"]

    result = []
    result.append(initial_text)

    for step in steps:
        html = step["html_instructions"]
        soup = BeautifulSoup(html, "html.parser")
        line = soup.get_text()
        result.append(line)
    text = "\n".join(result)
    return text
