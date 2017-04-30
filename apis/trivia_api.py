import requests

def get_trivia():
    '''
    Makes a Trivia API call to get a question and answer
    :return: a random trivia question with the answer
    '''
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