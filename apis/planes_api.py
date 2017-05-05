import random
from server import *

SEPARATOR = " "
NO_PLANES_MESSAGE = "No planes flying! Try launching one?"
LAUNCH_MESSAGE = "Congrats! Your plane has been launched."
JOIN = " from "
SUFFIX = " says hi!"

def retrieve_plane():
    '''
    Retrieves a random plane instance from the database
    :return: the plane message if found, None otherwise
    '''
    planes = Planes.query.all()

    #return no planes message if no plane found
    if len(planes) == 0:
        return NO_PLANES_MESSAGE

    index = random.randint(0, len(planes)-1)
    plane = planes[index]
    user = plane.user
    country = plane.country
    message = user + JOIN + country + SUFFIX
    return message

def create_plane(user, country):
    '''
    Creates a new plane instance in the database
    :param user: the person launching the plane
    :param country: the country the person is from
    '''
    plane = Planes(user, country)
    db.session.add(plane)
    db.session.commit()

def is_valid_catch(text):
    '''
    Check if the given text for catching a plane is valid or not
    :param text: The user entered text for catching a plane
    :return: The text if valid, None otherwise
    '''
    text = text.strip()

    words = text.split(SEPARATOR)
    if len(words) != 1:
        return None

    if words[0].lower() != "catch":
        return None

    return text

def is_valid_launch(text, countries_dict):
    '''
    Check if the given text for launching a plane is valid or not
    :param text: The user entered text for launching a plane
    :param countries_dict: The dictionary with all the valid countries
    :return: The list of words if text is valid, None otherwise
    '''
    #remove any leading or trailing spaces from the string
    text = text.strip()

    #check the number of words in the launch text is at least 3
    if len(text.split(SEPARATOR)) < 3:
        return None

    #get the launch command and check if valid
    space = text.find(SEPARATOR)
    command = text[:space]
    if command.lower() != "launch":
        return None

    #get the user name
    text = text[space:].strip()
    space = text.find(SEPARATOR)
    user = text[:space]

    #get the country and check if valid
    text = text[space:].strip()
    country = text.lower()
    if country not in countries_dict:
        return None
    else:
        country = countries_dict[country]

    words = [command, user, country]
    return words

def launch_plane(text, countries_dict):
    '''
    Launch a plane with the user and the country given in the text if valid
    :param text: Adds the new plane to the database if valid
    :param countries_dict: The dictionary with all the valid countries
    :return: A message if plane is successfully launched, None otherwise
    '''

    #check the given text for launching a plane is valid
    words = is_valid_launch(text, countries_dict)

    #return None if the launch text is invalid
    if words is None:
        return None

    create_plane(words[1], words[2])
    return LAUNCH_MESSAGE

def catch_plane(text):
    '''
    Catch a plane
    :param text: The text to catch a plane
    :return: A random plane from the database if found, None otherwise
    '''

    #check if the given text for catching a plane is valid
    words = is_valid_catch(text)

    #return None if the catch text is invalid
    if words is None:
        return None

    result = retrieve_plane()
    return result