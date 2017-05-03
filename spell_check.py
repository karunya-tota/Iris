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

def main():
    query = "Popular queries"
    print(check_spelling(query))

if __name__ == "__main__":
    main()
