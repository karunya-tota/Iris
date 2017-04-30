import requests

SEPARATOR = " "

def is_valid_query(text):
    '''
    Check if the query by the user is valid or not
    :param text: The query entered by the user
    :return: true if the query is "trivia", False otherwise
    '''
    text = text.strip()
    text = text.split(SEPARATOR)
    if len(text) != 1:
        return False
    query = text[0].lower()
    if query != "trivia":
        return False
    else:
        return True

def get_trivia(text):
    '''
    Makes a Trivia API call to get a question and answer
    :param text: The query entered by the user
    :return: a random trivia question with the answer
    '''

    if is_valid_query(text) == False:
        return None

    url = "https://opentdb.com/api.php?amount=1&type=multiple"

    response = requests.get(url)
    if response.status_code == 404 or response.status_code == 500:
        return None
    json = response.json()

    text = None
    if "results" in json:
        results = json["results"][0]
        if "question" in results:
            question_prefix = "Question: "
            answer_prefix = "Answer: "
            question = results["question"]
            answer = results["correct_answer"]
            text = [question_prefix, question, answer_prefix, answer]
            text = "\n".join(text)

    if text is not None:
        return text
    else:
        return None