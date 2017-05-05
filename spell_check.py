import enchant

def check_spelling(text):
    '''
    Checks the spelling of given input text
    :param text: Input text (query)
    :return: boolean: spelling_correct: Returns whether the spelling is correct of the input text
    '''
    dictionary = enchant.Dict('en_US')
    words = text.split()
    spelling_correct = True

    for word in words:
        if dictionary.check(word) == False:
            spelling_correct = False

    return spelling_correct

def offer_suggestions(text):
    '''
    Offers suggestions for the spelling of the input text
    :param text: Input text (query)
    :return: suggestion: The suggest text with the correct spelling
    '''
    dictionary = enchant.Dict('en_US')
    words = text.split()
    suggestion_response = []

    for word in words:
        if check_spelling(word) == False:
            suggested_word = dictionary.suggest(word)

            if len(suggested_word) == 0:
                return ''
            suggestion_response.append(suggested_word[0])
        else:
            suggestion_response.append(word)

    suggested_response = " ".join(suggestion_response)

    return suggested_response


def main():
    query = "Popular queries"
    print(check_spelling(query))
    incorrect = "hellow girl"
    print(offer_suggestions(incorrect))

if __name__ == "__main__":
    main()
