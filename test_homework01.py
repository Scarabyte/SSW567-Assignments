#############################
#       SSW 567
#     Homework 01
#    Adam Burbidge
#############################
import unittest
from homework01 import *
from math import sqrt

class TestHomework01(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_isTriangle(self):
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
    
    def test_classifyTriangle_NotATriangle(self):
        #Test some non-triangles
        self.assertEqual(classifyTriangle(1,4,6),'NotATriangle')
    
    def test_classifyTriangle_Equilateral(self):
        #Test some Equilateral Triangles
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
    
    def test_classifyTriangle_Isosceles(self):
        #Test some Isosceles Triangles
        self.assertEqual(classifyTriangle(2, 2, 1),'Isosceles')
    
    def test_classifyTriangle_IsoscelesRight(self):
        #Test some Isosceles Right Triangles
        self.assertEqual(classifyTriangle(sqrt(2),sqrt(2),2),'IsoscelesRight')
    
    def test_classifyTriangle_Scalene(self):
        #Test some Scalene Triangles
        self.assertEqual(classifyTriangle(1,2,3),'Scalene')
    
    def test_classifyTriangle_ScaleneRight(self):
        #Test some Scalene Right Triangles
        self.assertEqual(classifyTriangle(3,4,5),'ScaleneRight')
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
