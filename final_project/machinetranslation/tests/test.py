import unittest
from translator import french_to_english, english_to_french

class TestingTranslator(unittest.TestCase):
    ## English to french tests
    def test_e2f_null(self):
        self.assertEqual(english_to_french(""), 'The string you entered is empty!\n')
    def test_e2f_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour\n')
    
    #French to english tests
    def test_f2e_null(self):
        self.assertEqual(french_to_english(""), 'Le texte que vous avez saisi est vide!\n')
    def test_f2e_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello\n')

unittest.main()