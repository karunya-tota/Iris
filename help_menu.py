def get_help_menu():
    options = ["Welcome to Iris!",
               "We support the following Functionalities:",
               "1. Google Maps",
               "2. Weather",
               "3. News",
               "4. Recipe",
               "5. Definition",
               "6. Pronunciation",
               "7. Jokes",
               "8. Numbers",
               "9. Trivia",
               "10. Popular Queries",
               "11. Launch or Catch Planes",
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
                 "News from The New York Times\n" \
                 "Sources: ABC News, Al Jazeera, ARS Technica , Associated Press, BBC News, BBC Sports, Bild , Bloomberg, Breitbart News, Business Insider, Business Insider UK, Buzzfeed, CNBC News, CNN News, Daily Mail Newsm Der-Tagesspiegel, Die Zeit,En gadget, Entertainment Weekly, ESPN, Financial Times, Focus, Football Italian, Fortune, FourFour, Fox Sports, Google News, Gruenderszene, Hacker News, Handelsblatt, IGN, Independent, Mashable, Metro, Mirror, MTV News, MTV News UK, National Geographic, New Scientist, Newsweek, New York Magazine, NFL News, Polygon, Recode, Reddit, Reuters, Spiegel Online, T3N, Talksport, Techcrunch, Techradar, The Economist, The Guardian AU, The Guardian UK, The Hindu, The Huffington Post, The Lad Bible, The New York Times, The Next Web, The Sport Bible, The Telegraph, The Times of India, The Verge, The Wall Street Journal, The Washington Post, The Time, Usa Today, Wired.de "
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
        result = "To get a fun fact about numbers, enter:\n" \
                 "Numbers Trivia or Numbers Year or Numbers Date or Numbers Month"
    elif text == "9":
        result = "To get a trivia question, enter:\n" \
                 "Trivia"
    elif text == "10":
        result = "To get Popular queries, enter:\n" \
                 "Popular queries or Popular queries in <category>"
    elif text == "11":
        result = "To launch a plane, enter:\n" \
                 "Launch <your name> <your country>\n" \
                 "To catch a plane, enter:\n" \
                 "Catch\n" \

    return result
