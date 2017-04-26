import unittest
from apis.weather_api import *


class TestWeatherAPI(unittest.TestCase):
    """
    Open Weather Map API Test Cases Class
    """
    def test_missing_prefix(self):
        '''
        Tests if the text is processed when the prefix 'Weather at' is missing
        '''
        text = 'Weather Orlando'
        location = find_location(text)
        self.assertIsNone(location)

        text2 = 'Weather in Orlando'
        location = find_location(text)
        self.assertIsNone(location)

    def test_invalid_text(self):
        '''
        Tests if an Invalid Request message is returned for invalid location
        '''
        text = 'Weather at aslsdkfj'
        response = get_weather(text)
        self.assertEqual(response, "Invalid Request. Check syntax and try again!")

    def test_make_request(self):
        '''
        Tests if a request is successfully made
        '''
        text = 'Weather at Orlando'
        location = find_location(text)
        self.assertEqual(location, 'Orlando')

        response = get_weather(text)
        self.assertIn('Weather:', response)
        self.assertIn('Description:', response)
        self.assertIn('Humiditiy:', response)
        self.assertIn('Wind Speed:', response)

if __name__ == '__main__':
    unittest.main()
