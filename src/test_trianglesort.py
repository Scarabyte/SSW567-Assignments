#######################
#       SSW 567       #
#     Homework 04     #
#    Adam Burbidge    #
#######################
import unittest
from trianglesort import *


class TestHomework01(unittest.TestCase):
    """This class tests the functions in the trianglesort.py file."""

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
        self.assertEqual(classify_triangle(1, 4, 6), 'Not A Triangle')

    def test_classify_triangle_Equilateral(self):
        """Test some Equilateral Triangles"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral Triangle')

    def test_classify_triangle_Isosceles(self):
        """Test some Isosceles Triangles"""
        self.assertEqual(classify_triangle(2, 2, 1), 'Isosceles Triangle')

    def test_classify_triangle_IsoscelesRight(self):
        """Test some Right Isosceles Triangles"""
        self.assertEqual(classify_triangle(sqrt(2), sqrt(2), 2),
                         'Right Isosceles Triangle')

    def test_classify_triangle_Scalene(self):
        """Test some Scalene Triangles"""
        self.assertEqual(classify_triangle(1, 2, 3), 'Scalene Triangle')

    def test_classify_triangle_ScaleneRight(self):
        """Test some Right Scalene Triangles"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene Triangle')

    def test_classify_triangle_non_integer_numbers(self):
        """Test some triangles that do not have integer-length sides"""
        self.assertEqual(classify_triangle(2.5, 3.4, 7.6), 'Not A Triangle')
        self.assertEqual(classify_triangle(2.5, 3.4, 5.1), 'Scalene Triangle')

    def test_classify_triangle_zero(self):
        """Test the classify_triangle function with zero-length sides"""
        self.assertEqual(classify_triangle(3, 0, 5), 'Not A Triangle')
        self.assertEqual(classify_triangle(0, 123, 0), 'Not A Triangle')
        self.assertEqual(classify_triangle(5.23461, 0, 0), 'Not A Triangle')

    def test_classify_triangle_negative_numbers(self):
        """Test the classify_triangle function with some negative numbers"""
        self.assertEqual(classify_triangle(-1, 123, 3.14), 'Not A Triangle')
        self.assertEqual(classify_triangle(1, -123, 300), 'Not A Triangle')

    @unittest.expectedFailure
    def test_classify_triangle_big_numbers(self):
        """Test the classify_triangle function with "big" numbers"""
        self.assertEqual(classify_triangle(10000000,
                                           9999999,
                                           10), 'Scalene Triangle')
        self.assertEqual(classify_triangle(9999999.999999,
                                           9999999.999999,
                                           9999999.999999),
                         'Equilateral Triangle')
        self.assertEqual(classify_triangle(10000000.0000001,
                                           10000000,
                                           20.652), 'Scalene Triangle')
        self.assertEqual(classify_triangle(10000000.001,
                                           10000000.001,
                                           0.1), 'Isosceles Triangle')

    @unittest.expectedFailure
    def test_classify_triangle_big_numbers_expected_failures(self):
        """Test classify_triangle with large "out of tolerance" numbers"""
        # Implementer's notes: These tests are expected to fail because
        # the function as currently implemented is not really equipped
        # to handle this type of input. However, after discussions with
        # the customer to clarify the requirements and determin the actual
        # needs for the function, it is possible that the implementation
        # may change; in such a case, these tests may subsequently pass
        # without requiring any changes to the tests themselves.
        self.assertEqual(classify_triangle(10000000.0001,
                                           10000000.0001,
                                           0.01), 'Isosceles Triangle',
                         'Out of tolerance when squared')

    def test_classify_triangle_small_numbers(self):
        """Test the classify_triangle function with "small" numbers"""
        self.assertEqual(classify_triangle(0.0000001,
                                           0.0000002,
                                           0.000001), 'Not A Triangle')
        self.assertEqual(classify_triangle(0.001,
                                           0.002,
                                           0.002), 'Isosceles Triangle')
        self.assertEqual(classify_triangle(0.0000001, 0.0000001, 0.0000001),
                         'Equilateral Triangle')
        self.assertEqual(classify_triangle(0.0001, 0.0001, 0.0001),
                         'Equilateral Triangle')

    @unittest.expectedFailure
    def test_classify_triangle_small_numbers_expected_failures(self):
        """Test the classify_triangle function with "too small" numbers"""
        # Implementer's note: These are considered expected failures
        # because they involve values smaller than the stated tolerance
        # of 1E-07, and therefore are not expected to succeed.
        # However the tolerance has not been approved by the customer,
        # and so may be changed to a different value as necessary to suit
        # the customer's needs. In such a case, it is possible that these
        # tests will pass without requiring any changes themselves.
        self.assertEqual(classify_triangle(0.00000011,
                                           0.00000012,
                                           0.000000123), 'Equilateral Triangle',
                         "Out of Stated Tolerance")
        self.assertEqual(classify_triangle(0.0001,
                                           0.0002,
                                           0.0002), 'Isosceles Triangle',
                         "Out of Stated Tolerance when squared")


if __name__ == '__main__':
    unittest.main(verbosity=2)
