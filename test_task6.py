#Andreas Xeni, U244N0653

import unittest
from my_functions import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0),1)
    
    def test_factorial_positive_small(self):
        self.assertEqual(factorial(3),6)

    def test_factorial_negative(self):
        self.assertRaises(ValueError)
    
if __name__=='__main__':
    unittest.main()