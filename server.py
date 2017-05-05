from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from twilio.twiml.messaging_response import MessagingResponse
from apis.chuck_norris_api import *
from apis.dictionary_api import *
from apis.google_maps_api import *
from apis.news_api import *
from apis.numbers_api import *
from apis.planes_api import *
from apis.recipes_api import *
from apis.trivia_api import *
from apis.weather_api import *
from help_menu import *
from spell_check import *

app = Flask(__name__)

invalid_syntax_message = "Invalid Request.\n" \
                         "Type \"help me\" or try again!"

# Loading the list of countries from a file into a dictionary
global ccountries_filename
countries_filename = "https://raw.githubusercontent.com/kaytota/Iris/master/countries.txt"
global countries_dict
countries_dict = {}

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///queries.sqlite3'
global db
db = SQLAlchemy(app)

class Queries(db.Model):
    '''
    Database model for a Query
    '''
    __tablename__ = 'queries_table'
    id = db.Column(db.Integer, primary_key='True')
    text = db.Column(db.String)
    count = db.Column(db.Integer)
    category = db.Column(db.String)

    def __init__(self, text, category):
        self.text = text
        self.category = category
        self.count = 1

    def increment(self):
        self.count += 1

class Planes(db.Model):
    '''
    Database model for a Plane
    '''
    __tablename__ = 'planes_table'
    id = db.Column(db.Integer, primary_key='True')
    user = db.Column(db.String)
    country = db.Column(db.String)

    def __init__(self, user, country):
        self.user = user
        self.country = country

# Creates both Queries table in the database
db.create_all()

def create_or_update_query(text, category):
    '''
    Creates a new query instance in the database or updates existing one
    :param text: User's requested query
    :return: None
    '''
    queries = Queries.query.filter_by(text=text).all()

    if len(queries) > 0:
        query = queries[0]
        query.increment()
        db.session.commit()

    else:
        query = Queries(text, category)
        db.session.add(query)
        db.session.commit()

    return None

def get_popular_queries():
    '''
    Retrieves the popular queries requested by users
    :return: response for SMS request for 'Popular queries'
    '''
    queries = Queries.query.all()

    if len(queries) == 0:
        return "No queries in database"

    queries = sorted(queries, key=lambda query: query.count, reverse=True)

    result = []
    num = 1

    for query in queries:
        if num > 5:
            break
        query_line = str(num) + ". " + query.text + ", hits: " + str(query.count)
        result.append(query_line)
        num += 1

    response = "\n".join(result)

    return response

def get_popular_queries_in_category(text):
    '''
    Retrieves the popular queries by cateogry
    :param text: SMS request input
    :return: response for SMS request Popular queries in <category>
    '''
    category = text[19:]
    queries = Queries.query.filter_by(category=category).all()

    queries = sorted(queries, key=lambda query: query.count, reverse=True)

    result = []
    result.append('Popular Queries ' + '(' + category + ')')
    num = 1

    for query in queries:
        if num > 5:
            break
        query_line = str(num) + ". " + query.text + ", hits: " + str(query.count)
        result.append(query_line)
        num += 1

    response = "\n".join(result)

    return response

@app.route("/", methods=['GET', 'POST'])
def send_response():
    '''
    Sends a response to the user when they reply to a message sent from Twilio
    :return: string of response sent to user
    '''
    text = str(request.values.get("Body", None))
    category = None
    response_body = None
    not_query_flag = 0

    if text.lower() == "help me":
        response_body = get_help_menu()
        not_query_flag = 1
    elif text[0].isdigit():
        response_body = get_syntax(text)
        not_query_flag = 1
    elif 'Directions' in text:
        category = 'Directions'
        response_body = get_directions(text)
    elif 'Weather' in text:
        response_body, not_query_flag = spell_check(text)
        category = 'Weather'
        if response_body is not None:
            response_body = get_weather(text)
    elif 'News' in text:
        category = 'News'
        response_body = get_news(text)
    elif 'Recipe' in text:
        response_body, not_query_flag = spell_check(text)
        category = 'Recipe'
        if response_body is not None:
            response_body = get_recipe(text)
    elif "Define" in text or "Pronounce" in text:
        response_body, not_query_flag = spell_check(text)
        category = 'Define'
        if response_body is not None:
            response_body = get_definition(text)
    elif "Jokes" in text or "Be funny" in text or "Chuck Norris" in text:
        category = 'Jokes'
        response_body = get_jokes()
    elif "Numbers" in text:
        category = 'Numbers'
        response_body = get_numbers(text)
    elif "Trivia" in text:
        category = 'Trivia'
        response_body = get_trivia(text)
    elif "Popular queries" == text:
        response_body = get_popular_queries()
        not_query_flag = 1
    elif "Popular queries in" in text:
        response_body = get_popular_queries_in_category(text)
        not_query_flag = 1
    elif "Launch" in text:
        response_body = launch_plane(text, countries_dict)
        not_query_flag = 1
    elif "Catch" in text:
        response_body = catch_plane(text)
        not_query_flag = 1

    if response_body is None:
        response_body = invalid_syntax_message
        not_query_flag = 1

    if not_query_flag == 0 :
        create_or_update_query(text, category)

    return return_response(response_body)

def spell_check(text):
    if check_spelling(text) == False:
        suggested_response = offer_suggestions(text)
        not_query_flag = 1
        if suggested_response != '':
            return return_response('Invalid Request. Perhaps, you meant \"' + suggested_response + '\" , or please try again!'), not_query_flag
        else:
            return return_response('Invalid Request. Please try again!'), not_query_flag
    else:
        return None

def return_response(text):
    response = MessagingResponse().message(text)
    result = str(response)

    return result

@app.route("/send_message", methods=['GET'])
def send_message():
    '''
    Renders the front-end view for Send Message View
    :return:
    '''
    result = render_template('message.html')
    return result

def load_countries():
    '''
    Loads all the countries from the github repo into a dictionary
    '''
    global countries_filename
    r = requests.get(countries_filename)

    lines = r.text
    lines = lines.split("\n")

    global countries_dict
    for line in lines:
        line_lower = line.lower()
        countries_dict[line_lower] = line

if __name__ == "__main__":
    load_countries()
    app.run(debug=True)
