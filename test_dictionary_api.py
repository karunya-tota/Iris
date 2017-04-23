import unittest
from dictionary_api import *

class TestDictionaryAPI(unittest.TestCase):
    """
    Oxford Dictionary API Test Cases Class
    """
    def test_invalid_number_of_words(self):
        '''
        Test if number of words in the query is not equal to 2 and invalid
        '''
        text1 = "Define programming studio"
        command, word = process_text(text1)
        self.assertEqual(command, None)
        self.assertEqual(word, None)

        text2 = 'Pronounce final project'
        command, word = process_text(text2)
        self.assertEqual(command, None)
        self.assertEqual(word, None)

    def test_valid_number_of_words(self):
        '''
        Test if the query is processed with the valid number of words
        '''
        text1 = "Define Programming"
        command, word = process_text(text1)
        self.assertEqual(command, "define")
        self.assertEqual(word, "programming")

        text2 = 'Pronounce Project'
        command, word = process_text(text2)
        self.assertEqual(command, "pronounce")
        self.assertEqual(word, "project")

    def test_invalid_command(self):
        '''
        Test if the query fails with an invalid command
        '''
        text = 'Definetion aficionado'
        result = get_definition(text)
        self.assertEqual(result, None)

    def test_invalid_word(self):
        '''
        Test if the query fails with an invalid word not in dictionary
        '''
        text = 'Define Aviato'
        result = get_definition(text)
        self.assertEqual(result, None)

    def test_define_valid_word(self):
        '''
        Test if the query is processed and definitions given for a valid word
        '''
        text = 'Define Aficionado'
        expected_definition = "Spelling: aficionado\n" \
        "Definitions: a person who is very knowledgeable and enthusiastic about an activity, subject, or pastime"
        result = get_definition(text)
        self.assertEqual(result, expected_definition)

    def test_pronounce_valid_word(self):
        '''
        Test if the query is processed and pronunciations given for a valid word
        '''
        text = 'Pronounce Aficionado'
        expected_pronunciation = "Spelling: aficionado\n" \
        "Phonetic Spelling: əˌfɪsjəˈnɑːdəʊ\n" \
        "Audio File Link: http://audio.oxforddictionaries.com/en/mp3/aficionado_gb_1_4.mp3"
        result = get_definition(text)
        self.assertEqual(result, expected_pronunciation)

if __name__ == '__main__':
    unittest.main()
