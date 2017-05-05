import unittest
from spell_check import *

class TestsSpellCheck(unittest.TestCase):
    """
    SMS API Test Cases Class
    """
    def test_check_spelling(self):
        '''
        Tests whether a text query is spelled correctly
        '''
        self.assertTrue(check_spelling('Hello'))
        self.assertFalse(check_spelling('Helo'))

    def test_check_suggestions(self):
        '''
        Tests whether a Twilio message returns an error when the to_number is not verified with Twilio
        :return:
        '''
        suggestion = offer_suggestions('hellow')
        self.assertEqual(suggestion, 'hello')

if __name__ == '__main__':
    unittest.main()
