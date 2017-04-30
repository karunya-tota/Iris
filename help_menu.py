def get_help_menu():
    options = ["Welcome to Iris!",
               "We support the following APIs:",
               "1. Google Maps",
               "2. Weather",
               "3. News",
               "4. Recipe",
               "5. Definition",
               "6. Pronunciation",
               "7. Jokes",
               "8. Trivia",
               "9. Popular Queries",
               "Enter one of the numbers for more info"]
    result = "\n".join(options)
    return result

def get_syntax(text):
    result = None
    if text == "1":
        result = "To get directions from Illini Union to Live Latitude, enter:\n" \
                 "Directions from Illini Union to Live Latitude"
    elif text == "2":
        result = "To check the weather in Chicago, enter:\n" \
                 "Weather in Chicago"
    elif text == "3":
        result = "To check the news from The New York Times, enter:\n" \
                 "News from The New York Times"
    elif text == "4":
        result = "To get the recipe for Chocolate Cake, enter:\n" \
                 "Recipe for Chocolate Cake"
    elif text == "5":
        result = "To get the definition of aficionado, enter:\n" \
                 "Define aficionado"
    elif text == "6":
        result = "To get the pronunciation of salmon, enter:\n" \
                 "Pronounce salmon"
    elif text == "7":
        result = "To get Chuck Norris jokes, enter:\n" \
                 "Jokes or Be funny or Chuck Norris"
    elif text == "8":
        result = "To get a trivia question, enter:\n" \
                 "Trivia"
    elif text == "9":
        result = "To get Popular queries, enter:\n" \
                 "Popular queries"
    return result
