from google_maps_api import *
from weather_api import *
from news_api import *
from recipes_api import *
from dictionary_api import *
from chuck_norris_api import *
from help_menu import *
from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

invalid_syntax_message = "Invalid Request.\n" \
                         "Type \"help me\" or try again!"

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///queries.sqlite3'
db = SQLAlchemy(app)

class Queries(db.Model):
    '''
    Database model for a Comment
    '''
    __tablename__ = 'queries_table'
    id = db.Column(db.Integer, primary_key='True')
    text = db.Column(db.String)
    count = db.Column(db.Integer)

    def __init__(self, text):
        self.text = text
        self.count = 1

    def increment(self):
        self.count += 1

# Creates both Queries table in the database
db.create_all()

def create_or_update_query(text):
    '''
    Creates a new query instance in the database or updates existing one
    :param text: User's requested query
    :return: None
    '''
    queries = Queries.query.filter_by(text=text).all()

    if len(queries) > 0:
        query = queries[0]
        query.increment()
        print(query.text)
        print(query.count)
        db.session.commit()

    else:
        query = Queries(text)
        db.session.add(query)
        print(query.text)
        print(query.count)
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

@app.route("/", methods=['GET', 'POST'])
def send_response():
    '''
    Sends a response to the user when they reply to a message sent from Twilio
    :return: string of response sent to user
    '''
    text = str(request.values.get("Body", None))
    response_body = None
    not_query_flag = 0

    if text.lower() == "help me":
        response_body = get_help_menu()
        not_query_flag = 1
    elif text[0].isdigit():
        response_body = get_syntax(text)
        not_query_flag = 1
    elif 'Directions' in text:
        response_body = get_directions(text)
    elif 'Weather' in text:
        response_body = get_weather(text)
    elif 'News' in text:
        response_body = get_news(text)
    elif 'Recipe' in text:
        response_body = get_recipe(text)
    elif "Define" in text or "Pronounce" in text:
        response_body = get_definition(text)
    elif "Jokes" in text or "Be funny" in text or "Chuck Norris" in text:
        response_body = get_jokes()
    elif "Popular" in text:
        response_body = get_popular_queries()
        not_query_flag = 1

    if response_body is None:
        response_body = invalid_syntax_message

    response = MessagingResponse().message(response_body)

    if not_query_flag == 0 :
        create_or_update_query(text)

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

if __name__ == "__main__":
    app.run(debug=True)
