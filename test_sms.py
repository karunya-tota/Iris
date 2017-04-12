import unittest
from sms import *

class TestsSMS(unittest.TestCase):
    """
    SMS API Test Cases Class
    """
    def test_send_message(self):
        '''
        Tests whether a Twilio message is successfully sent
        '''
        message = send_message('+13213550503', 'Hello World!')
        self.assertEqual(message.body, 'Sent from your Twilio trial account - Hello World!')
        self.assertEqual(message.status, 'queued')
        self.assertEqual(message.from_, '+13214183889')
        self.assertEqual(message.to, '+13213550503')

    def test_send_message_unverified_number(self):
        '''
        Tests whether a Twilio message returns an error when the to_number is not verified with Twilio
        :return:
        '''
        message = send_message('+14077398682', 'Hello World!')
        self.assertEqual(message, 'Unverified Phone Number!')

if __name__ == '__main__':
    unittest.main()
