#Andreas Xeni, U244N0653    

import unittest
from my_functions import add, subtract

class testAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(1,2),3)

    def test_negative_numbers(self):
        self.assertEqual(add(-1,-2),-3)

    def test_zero(self):
        self.assertEqual(add(0,1),1)

class testSubtract(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(subtract(3,2),1)

    def test_negative_numbers(self):
        self.assertEqual(subtract(-3,-2),-1)

    def test_zero(self):
        self.assertEqual(subtract(0,1),-1)


if __name__=='__main__':
    unittest.main()