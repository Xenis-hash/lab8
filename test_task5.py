#Andreas Xeni, U244N0653

import unittest
from my_functions import max_numbers

class TestFindMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_numbers([4,8,25,86,99,5]),99)
    
    def test_negative_numbers(self):
        self.assertEqual(max_numbers([-2,-26,-46,-88,-36]),-2)

    def test_single_element(self):
        self.assertEqual(max_numbers([2]),2)

    def test_sorted_list(self):
        self.assertEqual(max_numbers([1,2,3,4,5,6]),6)

    def test_reverse_sorted_list(self):
        self.assertEqual(max_numbers([6,5,4,3,2,1]),6)

    
    if __name__=='__main__':
        unittest.main()