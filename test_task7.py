#Andreas Xeni, U244N0653

import unittest
from my_functions import sort_numbers

class TestSortNumbers(unittest.TestCase):
    def test_already_sorted(self):
        self.assertEqual(sort_numbers([1,2,3,4,5]),[1,2,3,4,5])
    
    def test_reverse_sorted(self):
        self.assertEqual(sort_numbers([5,4,3,2,1]),[1,2,3,4,5])
    
    def test_with_duplicates(self):
        self.assertEqual(sort_numbers([2,3,7,5,6,2,3]),[2,2,3,3,5,6,7])

    def test_empty_list(self):
        self.assertEqual(sort_numbers([]),[])
    
if __name__=='__main__':
    unittest.main()