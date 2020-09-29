import unittest
import calc

class testCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(1,1)
        self.assertEqual(result, 2) 
        self.assertEqual(calc.add(-1,1), 0)

    def test_subtract(self):
        result = calc.subtract(10,5)
        self.assertEqual(result, 5)

        
if __name__ == '__main__':
    unittest.main()