import unittest
from apis.google_maps_api import *


class TestGoogleMapsAPI(unittest.TestCase):
    """
    Google Maps API Test Cases Class
    """
    def test_missing_prefix(self):
        '''
        Tests if the text is processed when the prefix 'Directions from' is missing
        '''
        text = 'Instructions to get to Illini Union from Latitude Apartments'
        start, end = process_text(text)
        self.assertIsNone(start)
        self.assertIsNone(end)

        text2 = 'Directions from Illini Union'
        start2, end2 = process_text(text)
        self.assertIsNone(start2)
        self.assertIsNone(end2)

    def test_missing_separator(self):
        '''
        Tests if the text is processed when the separator 'to' is missing
        '''
        text = 'Directions from Illini Union from Latitude Apartments'
        start, end = process_text(text)
        self.assertIsNone(start)
        self.assertIsNone(end)

    def test_matching_start_end_points(self):
        '''
        Tests if the text is processed when the start and end points are matching
        '''
        text = 'Directions from Illini Union to Illini Union'
        start, end = process_text(text)
        self.assertIsNone(start)
        self.assertIsNone(end)

    def test_invalid_text(self):
        '''
        Tests if an Invalid Request message is returned for invalid start and end points
        '''
        text = 'Directions from aslsdkfj to alsjdf'
        response = make_request(text)
        self.assertEqual(response, "Invalid Request. Check syntax and try again!")

    def test_make_request(self):
        '''
        Tests if a request is successfully made
        '''
        text = 'Directions from Illini Union to Latitude Apartments UIUC'
        start, end = process_text(text)
        self.assertEqual(start, 'Illini Union')
        self.assertEqual(end, 'Latitude Apartments UIUC')

        response = make_request(text)
        expected_response = "Directions:\nHead south\nTurn right onto W Green St\nTurn left at the 1st cross street onto S Mathews Ave\nTurn left onto W University Ave\nContinue straight onto E University AveDestination will be on the right"
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
