import unittest
import special_method

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(special_method.add(20, 5), 25)
        self.assertEqual(special_method.add(-1, 1), 0)
        self.assertEqual(special_method.add(-1, -1), -2)
        
    def test_subtract(self):
        self.assertEqual(special_method.subtract(20, 5), 15)
        self.assertEqual(special_method.subtract(-1, 1), -2)
        self.assertEqual(special_method.subtract(-1, -1), 0)
        
    def test_divide(self):
        self.assertEqual(special_method.divide(20, 5), 4)
        self.assertEqual(special_method.divide(-1, 1), -1)
        self.assertEqual(special_method.divide(-1, -1), 1)
        
        #to raise zero division error
        with self.assertRaises(ZeroDivisionError):
            special_method.divide(2, 0)
            
    def test_multiply(self):
        self.assertEqual(special_method.multiply(20, 5), 100)
        self.assertEqual(special_method.multiply(-1, 1), -1)
        self.assertEqual(special_method.multiply(-1, -1), 1)
        
        
if __name__ == '__main__':
    unittest.main()
    #unittest.main(argv=['first-arg-is-ignored'], exit=False)