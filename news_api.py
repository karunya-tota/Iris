import requests

#API Documentation:https://newsapi.org

API_ENDPOINT = "https://newsapi.org/v1/articles?"
API_KEY = "e3de538e9b424cd5b527f6ea59248212"
SOURCES = {
           	   "ABC News" : "abc-news-au",
           "Al Jazeera": "al-jazeera-english",
           "ARS Technica" : "ars-technica",
           "Associated Press" : "associated-press",
           "BBC News" : "bbc-news",
           "BBC Sports" : "bbc-sport",
           "Bild" : "bild",
           "Bloomberg" : "bloomberg",
           "Breitbart News" : "breitbart-news",
           "Business Insider" : "business-insider",
           "Business Insider UK" : "business-insider-uk",
           "Buzzfeed" : "buzzfeed",
           "CNBC News" : "cnbc",
           "CNN News" : "cnn",
           "Daily Mail News": "daily-mail",
           "Der-Tagesspiegel" : "der-tagesspiegel",
           "Die Zeit" : "die-zeit",
           "Engadget" : "engadget",
           "Entertainment Weekly" : "entertainment-weekly",
           "ESPN" : "espn",
           "Financial Times" : "financial-times",
           "Focus" : "focus",
           "Football Italian" : "football-italia",
           "Fortune" : "fortune",
           "FourFour" : "four-four-two",
           "Fox Sports" : "fox-sports",
           "Google News" : "google-news",
           "Gruenderszene" : "gruenderszene",
           "Hacker News" : "hacker-news",
           "Handelsblatt" : "handelsblatt",
           "IGN" : "ign",
           "Independent" : "independent",
           "Mashable" : "mashable",
           "Metro" : "metro",
           "Mirror" : "mirror",
           "MTV News" : "mtv-news",
           "MTV News UK" : "mtv-news-uk",
           "National Geographic" : "national-geographic",
           "New Scientist" : "new-scientist",
           "Newsweek" : "newsweek",
           "New York Magazine" : "new-york-magazine",
           "NFL News" : "nfl-news",
           "Polygon" : "polygon",
           "Recode" : "recode",
           "Reddit" : "reddit-r-all",
           "Reuters" : "reuters",
           "Spiegel Online" : "spiegel-online",
           "T3N" : "t3n",
           "Talksport" : "talksport",
           "Techcrunch" : "techcrunch",
           "Techradar" : "techradar",
           "The Economist" : "the-economist",
           "The Guardian AU" : "the-guardian-au",
           "The Guardian UK" : "the-guardian-uk",
           "The Hindu" : "the-hindu",
           "The Huffington Post" : "the-huffington-post",
           "The Lad Bible" : "the-lad-bible",
           "The New York Times" : "the-new-york-times",
           "The Next Web" : "the-next-web",
           "The Sport Bible" : "the-sport-bible",
           "The Telegraph" : "the-telegraph",
           "The Times of India" : "the-times-of-india",
           "The Verge" : "the-verge",
           "The Wall Street Journal" : "the-wall-street-journal",
           "The Washington Post" : "the-washington-post",
           "The Time" : "time",
           "Usa Today" : "usa-today",
           "Wired.de" : "wired-de",
        }


prefix = "News from "

invalid_syntax_message = "Invalid Request. Check syntax and try again!"

def find_news_source(text):
    '''
    Returns the daily news from the provided source
    :param text: Requested News Source
    :return: news: Daily news from source
    '''
    index = text.find(prefix)

    if index < 0:
        return None

    news_source = text[len(prefix):]

    return news_source

def retrieve_request_url(news_source):
    '''
    Retireves the request url for the News Api given the news source
    :param news_source: The source of the requested news
    :return: url: The News API request url
    '''
    url = API_ENDPOINT + "source=" + news_source + "&" + "apiKey=" + API_KEY

    return url

def format_response(news_source, json):
    '''
    Formats the response from the news api
    :param news_source: The source of the requested news
    :param json: The json response from the api call
    :return: response: The response to be displayed in the SMS message
    '''

    result = []
    num = 1

    result.append(news_source + ":")

    for article in json['articles']:
        if(num > 5):
            break
        new_entry = str(num) + '. ' + article['title'] + ':'
        new_description = "--- \"" + article['description'] + "\""
        result.append(new_entry)
        result.append(new_description)
        num += 1

    response = "\n".join(result)

    return response

def get_news(text):
    '''
    Makes a News API request provided the source from the user
    :param text: The source of news requested
    :return: text: Daily news from requested source
    '''
    news_source = find_news_source(text)

    if news_source is None or news_source not in SOURCES:
        return invalid_syntax_message

    url = retrieve_request_url(SOURCES[news_source])

    response = requests.get(url)
    json = response.json()

    if json['status'] != "ok":
        return invalid_syntax_message

    response = format_response(news_source, json)

    return response

def main():
    print(get_news('Daily News from The New York Times'))

if __name__ == "__main__":
    main()
