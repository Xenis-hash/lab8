#Andreas Xeni, U244N0653

import unittest
from my_functions import reverse_string

class testReverseString(unittest.TestCase):
    def test_normal_string(self):
        self.assertEqual(reverse_string('manish'),'hsinam')
    
    def test_empty_string(self):
        self.assertEqual(reverse_string(''),'')

    def test_palindrome_string(self):
        self.assertEqual(reverse_string('madam'),'madam')

if __name__=='__main__':
    unittest.main()
        