import unittest
from apis.news_api import *


class TestNewsAPI(unittest.TestCase):
    """
    News API Test Cases Class
    """
    def test_missing_prefix(self):
        '''
        Tests if the text is processed when the prefix 'News from' is missing
        '''
        text = 'News Fortune'
        news_source = find_news_source(text)
        self.assertIsNone(news_source)

        text2 = 'The New York Times'
        news_source = find_news_source(text)
        self.assertIsNone(news_source)

    def test_invalid_text(self):
        '''
        Tests if an Invalid Request message is returned for invalid news source
        '''
        text = 'News from India'
        response = get_news(text)
        self.assertEqual(response, "Invalid Request. Check syntax and try again!")

    def test_make_request(self):
        '''
        Tests if a request is successfully made
        '''
        text = 'News from The New York Times'
        news_source = find_news_source(text)
        self.assertEqual(news_source, 'The New York Times')

        response = get_news(text)
        self.assertIn('News:', response)
        self.assertIn('1. ', response)
        self.assertIn('2. ', response)
        self.assertIn('3. ', response)
        self.assertIn('4. ', response)
        self.assertIn('5. ', response)

if __name__ == '__main__':
    unittest.main()
