"""_summary_
    - testing the translator function in translate.py using unittest
    - each function will have 2 test cases
    - each test case will have 2 assertions (equal and notEqual)
"""
import unittest
import sys , os
#import machinetranslation from the parent directory
sys.path.append(os.path.dirname(os.getcwd()))
import machinetranslation
import machinetranslation.translator
from machinetranslation.translator import english_to_french,french_to_english

class TestTranslate(unittest.TestCase):
    """
     this class is created to init the test functions for the translator.py file
    """
    def test_english_to_french(self):
        """
        1- test when the function is called without any input the output is False.
        2- test when 'Hello' is given as input the output is 'Bonjour'.
        3- test when "car" is given as input the output is not 'Bonjour'.
        """
        self.assertEqual(english_to_french(),False)
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french("car"),'Bonjour')
    def test_french_to_english(self):
        """
        1- test when the function is called without any input the output is False.
        2- test when 'Bonjour' is given as input the output is 'Hello'.
        3- test when "voiture" is given as input the output is not 'Hello'. 
        """
        self.assertEqual(french_to_english(),False)
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english("voiture"),'Hello')
unittest.main()
#remove current working directory from the path
sys.path.remove(os.path.dirname(os.getcwd()))
