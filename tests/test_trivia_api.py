import unittest
from apis.trivia_api import *


class TestTriviaAPI(unittest.TestCase):
    """
    Trivia API Test Cases Class
    """
    def test_missing_prefix(self):
        '''
        Tests if the text is processed when the prefix 'Trivia' is missing and gets None
        '''
        text = 'Quiz'
        result = get_trivia(text)
        self.assertIsNone(result)

        text2 = 'Trivias'
        result = get_trivia(text)
        self.assertIsNone(result)

    def test_invalid_number_of_words(self):
        '''
        Tests if the query text contains less or more than 1 word and gets None
        '''
        text = 'Trivia Question'
        result = get_trivia(text)
        self.assertIsNone(result)

    def test_valid_choice(self):
        '''
        Tests if a valid query returns a Trivia question and answer
        '''
        text = 'Trivia'
        result = get_trivia(text)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
