#Andreas Xeni, U244N0653

import unittest
from my_functions import is_valid_password

class TestIsValidPassword(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(is_valid_password('Valid123'))
    def test_too_short(self):
        self.assertFalse(is_valid_password('Valid12'))
    def test_no_uppercase(self):
        self.assertFalse(is_valid_password('valid123'))
    def test_no_lowercase(self):
        self.assertFalse(is_valid_password('VALID123'))
    def test_no_digit(self):
        self.assertFalse(is_valid_password('validpassword'))
    

if __name__=='__main__':
    unittest.main()