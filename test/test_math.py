import unittest
from dev.math import Maths

class TestMath(unittest.TestCase):
    
    mth = Maths()
    
    def test_add_num(self):
        self.assertEqual(TestMath.mth.add_num(1, 2), 3)
        
    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            TestMath.mth.divide(0, 2)
            # self.assertEqual(str(exception_context), "denominator value is zero can not divide")
    
    def test_data(self):
        with self.assertRaises(ValueError) as exception_context:
            TestMath.mth.data(0)
            self.assertEqual(str(exception_context.exception), "less the 1 Error")            
        
        
if __name__ == '__main__':
    unittest.main()