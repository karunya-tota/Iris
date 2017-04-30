import unittest
from apis.numbers_api import *


class TestNumbersAPI(unittest.TestCase):
    """
    Numbers API Test Cases Class
    """
    def test_missing_prefix(self):
        '''
        Tests if the text is processed when the prefix 'Numbers' is missing and gets None
        '''
        text = 'Trivia Numbers'
        result = get_numbers(text)
        self.assertIsNone(result)

        text2 = 'Number Date'
        result = get_numbers(text)
        self.assertIsNone(result)

    def test_invalid_number_of_words(self):
        '''
        Tests if the query text contains less or more than 2 words and gets None
        '''
        text = 'Numbers for Date'
        result = get_numbers(text)
        self.assertIsNone(result)

    def test_invalid_choice(self):
        '''
        Tests if the query text contains an invalid choice and gets None
        '''
        text = 'Numbers Week'
        result = get_numbers(text)
        self.assertIsNone(result)

    def test_valid_choice(self):
        '''
        Tests if a valid query returns a numbers trivia
        '''
        text = 'Numbers Trivia'
        result = get_numbers(text)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
