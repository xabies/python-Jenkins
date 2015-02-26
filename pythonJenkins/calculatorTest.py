import random
import unittest

from calculator import Calculator



class CalculatorTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.c = Calculator()
        
    def test_add(self):
        self.assertEqual(8, self.c.add(5,3))

    def test_subtract(self):
        self.assertEqual(4, self.c.subtract(8,4))


if __name__ == '__main__':
    unittest.main()