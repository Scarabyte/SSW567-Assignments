#############################
#       SSW 567
#     Homework 01
#    Adam Burbidge
#############################
import unittest
from homework01 import *

class TestHomework01(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_istriangle(self):
        
        #Test some numbers that will and won't form triangles
        self.assertTrue(isTriangle(3,4,5))
        self.assertTrue(isTriangle(2,2,1))
        self.assertTrue(isTriangle(1,2,3))
        self.assertTrue(isTriangle(8,3,10))
        self.assertTrue(isTriangle(7,2,8))
        
        self.assertFalse(isTriangle(1,4,6))
        self.assertFalse(isTriangle(3,3,9))        
        self.assertFalse(isTriangle(1,2,5))
        self.assertFalse(isTriangle(8,2,12))
        self.assertFalse(isTriangle(5,2,9))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
