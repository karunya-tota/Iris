import requests

# API Documentation:https://developer.edamam.com/edamam-docs-recipe-api

API_ENDPOINT = "https://api.edamam.com/search?"
API_ID = "c31346ed"
API_KEY = "8f8ddfde6c9fd54070517b1396c3f12a"

prefix = "Recipe for "

initial_text = "Recipe:"
invalid_syntax_message = "Invalid Request. Check syntax and try again!"

def find_recipe_name(text):
    '''
    Returns the name of the requested recipe from a SMS request
    :param text: Input text to retrieve recipe name from
    :return: recipe: Name of recipe
    '''
    index = text.find(prefix)

    if index < 0:
        return None

    recipe_name = text[len(prefix):]

    return recipe_name

def retrieve_request_url(recipe_name):
    '''
    Retireves the request url for the Recipe Api given the recipe name
    :param recipe_name: The name of the recipe to search for
    :return: url: The Edamam Recipe Api request url
    '''
    url = API_ENDPOINT + "app_id=" + API_ID + "&" + "app_key=" + API_KEY + "&q=" + recipe_name
    return url


def format_response(json):
    '''
    Formats the response from an Edamam Recipe API call for the SMS response
    :param json: the json response from the API call
    :return: text: the message to be sent to the user
    '''
    result = []
    result.append(initial_text)

    result.append('Ingredients:')

    for ingredient in json['ingredientLines']:
        result.append('- ' + ingredient)

    result.append('Calories: ' + str(round(json['calories'], 2)))

    healthLabels = 'Health Labels: '
    labels = json['healthLabels']

    for l in range(len(labels)-1):
        healthLabels += labels[l] + ', '
    healthLabels += labels[len(labels)-1]

    result.append(healthLabels)

    response = "\n".join(result)

    return response


def get_recipe(text):
    '''
    Makes a Edamam Recipe Api call given a text message
    :param text: message in the form 'Recipe for item'
    :return: text: overall ingredients for item
    '''
    recipe_name = find_recipe_name(text)

    if recipe_name is None:
        return invalid_syntax_message

    url = retrieve_request_url(recipe_name)
    response = requests.get(url)
    json = response.json()


    if len(json['hits']) == 0:
        return invalid_syntax_message

    response = format_response(json['hits'][0]['recipe'])

    return response

def main():
    print(get_recipe('Recipe for Tiramisu'))

if __name__ == "__main__":
    main()
