#############################
#       SSW 567
#     Homework 01
#    Adam Burbidge
#############################
import unittest
from homework01 import *


class TestHomework01(unittest.TestCase):
    """This class tests the functions in the homework01.py file."""

    def setUp(self):
        pass

    def test_is_triangle_True(self):
        """Test some numbers that form triangles"""
        self.assertTrue(is_triangle(3, 4, 5))
        self.assertTrue(is_triangle(2, 2, 1))
        self.assertTrue(is_triangle(1, 2, 3))
        self.assertTrue(is_triangle(8, 3, 10))
        self.assertTrue(is_triangle(7, 2, 8))

    def test_is_triangle_False(self):
        """Test some numbers that don't form triangles"""
        self.assertFalse(is_triangle(1, 4, 6))
        self.assertFalse(is_triangle(3, 3, 9))
        self.assertFalse(is_triangle(1, 2, 5))
        self.assertFalse(is_triangle(8, 2, 12))
        self.assertFalse(is_triangle(5, 2, 9))

    def test_classify_triangle_NotATriangle(self):
        """Test some non-triangles"""
        self.assertEqual(classify_triangle(1, 4, 6), 'NotATriangle')

    def test_classify_triangle_Equilateral(self):
        """Test some Equilateral Triangles"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')

    def test_classify_triangle_Isosceles(self):
        """Test some Isosceles Triangles"""
        self.assertEqual(classify_triangle(2, 2, 1), 'Isosceles')

    def test_classify_triangle_IsoscelesRight(self):
        """Test some Isosceles Right Triangles"""
        self.assertEqual(classify_triangle(sqrt(2), sqrt(2), 2),
                         'IsoscelesRight')

    def test_classify_triangle_Scalene(self):
        """Test some Scalene Triangles"""
        self.assertEqual(classify_triangle(1, 2, 3), 'Scalene')

    def test_classify_triangle_ScaleneRight(self):
        """Test some Scalene Right Triangles"""
        self.assertEqual(classify_triangle(3, 4, 5), 'ScaleneRight')

    def test_classify_triangle_non_integer_numbers(self):
        """Test some triangles that do not have integer-length sides"""
        pass

    def test_classify_triangle_negative_numbers(self):
        """Test the classify_triangle function with some negative numbers"""
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
