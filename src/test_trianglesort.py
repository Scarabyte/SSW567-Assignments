#######################
#       SSW 567       #
#     Homework 05     #
#    Adam Burbidge    #
#######################
import unittest
from trianglesort import *  # pylint: disable=wildcard-import
# Note: Ignoring the wildcard import in PyLint because we do want to exercise
# every function in the module and be warned if there are any unused ones.


class TestHomework04(unittest.TestCase):
    """This class tests the functions in the trianglesort.py file."""

    def setUp(self):
        pass

    def test_validate_inputs_True(self):
        # Test Case 01
        """Test input validation"""
        self.assertTrue(validate_inputs(42))
        self.assertTrue(validate_inputs(3.141))
        self.assertTrue(validate_inputs(98.7))
        self.assertTrue(validate_inputs(.6180))
        self.assertTrue(validate_inputs("42.314"))

    def test_validate_inputs_Negative(self):
        # Test Case 02
        """Verify that negative numbers fail validation"""
        self.assertFalse(validate_inputs(-98.7))
        self.assertFalse(validate_inputs(-500))
        self.assertFalse(validate_inputs(-0.618))
        self.assertFalse(validate_inputs("-42.314"))

    def test_validate_inputs_TooBig(self):
        # Test Case 03
        """Verify that numbers that are "too big" fail validation"""
        self.assertFalse(validate_inputs(1234))
        self.assertFalse(validate_inputs(1001))
        self.assertFalse(validate_inputs(1000.01))

    def test_validate_inputs_NonNumeric(self):
        # Test Case 04
        """Verify that non-numeric inputs fail validation"""
        self.assertFalse(validate_inputs("555.123.4567"))
        self.assertFalse(validate_inputs("5i+3j"))
        self.assertFalse(validate_inputs("ABCD"))
        self.assertFalse(validate_inputs("+1-(800)-555-2468"))

    def test_is_triangle_True(self):
        # Test Case 05
        """Test some numbers that form triangles"""
        self.assertTrue(is_triangle(3, 4, 5))
        self.assertTrue(is_triangle(2, 2, 1))
        self.assertTrue(is_triangle(1, 2, 3))
        self.assertTrue(is_triangle(8, 3, 10))
        self.assertTrue(is_triangle(7, 2, 8))

    def test_is_triangle_False(self):
        # Test Case 06
        """Test some numbers that don't form triangles"""
        self.assertFalse(is_triangle(1, 4, 6))
        self.assertFalse(is_triangle(3, 3, 9))
        self.assertFalse(is_triangle(1, 2, 5))
        self.assertFalse(is_triangle(8, 2, 12))
        self.assertFalse(is_triangle(5, 2, 9))

    def test_classify_triangle_NotATriangle(self):
        # Test Case 07
        """Test some non-triangles"""
        self.assertEqual(classify_triangle(1, 4, 6), 'Not A Triangle')

    def test_classify_triangle_Equilateral(self):
        # Test Case 08
        """Test some Equilateral Triangles"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral Triangle')

    def test_classify_triangle_Isosceles(self):
        # Test Case 09
        """Test some Isosceles Triangles"""
        self.assertEqual(classify_triangle(2, 2, 1), 'Isosceles Triangle')

    def test_classify_triangle_IsoscelesRight(self):
        # Test Case 10
        """Test some Right Isosceles Triangles"""
        self.assertEqual(classify_triangle(sqrt(2), sqrt(2), 2),
                         'Right Isosceles Triangle')

    def test_classify_triangle_Scalene(self):
        # Test Case 11
        """Test some Scalene Triangles"""
        self.assertEqual(classify_triangle(1, 2, 3), 'Scalene Triangle')
        self.assertEqual(classify_triangle(2.5, 3.4, 5.1), 'Scalene Triangle')

    def test_classify_triangle_ScaleneRight(self):
        # Test Case 12
        """Test some Right Scalene Triangles"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene Triangle')

    def test_classify_triangle_non_integer_numbers(self):
        # Test Case 13
        """Test some triangles that do not have integer-length sides"""
        self.assertEqual(classify_triangle(2.5, 3.4, 7.6), 'Not A Triangle')
        self.assertEqual(classify_triangle(2.5, 3.4, 5.1), 'Scalene Triangle')

    def test_classify_triangle_zero(self):
        # Test Case 14
        """Test the classify_triangle function with zero-length sides"""
        self.assertEqual(classify_triangle(3, 0, 5), 'Not A Triangle')
        self.assertEqual(classify_triangle(0, 123, 0), 'Not A Triangle')
        self.assertEqual(classify_triangle(5.23461, 0, 0), 'Not A Triangle')

    def test_classify_triangle_negative_numbers(self):
        # Test Case 15
        """Test the classify_triangle function with some negative numbers"""
        self.assertEqual(classify_triangle(-1, 123, 3.14), 'Not A Triangle')
        self.assertEqual(classify_triangle(1, -123, 300), 'Not A Triangle')

    def test_classify_triangle_big_numbers(self):
        # Test Case 16
        """Test the classify_triangle function with "big" numbers"""
        self.assertEqual(classify_triangle(1000,
                                           999,
                                           10), 'Scalene Triangle')
        self.assertEqual(classify_triangle(999.999999,
                                           999.999999,
                                           999.999999),
                         'Equilateral Triangle')
        self.assertEqual(classify_triangle(1000.0000001,
                                           1000,
                                           20.652), 'Not A Triangle')
        self.assertEqual(classify_triangle(1000.001,
                                           1000.001,
                                           0.1), 'Not A Triangle')

    def test_classify_triangle_small_numbers(self):
        # Test Case 17
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

    def test_classify_triangle_tolerance(self):
        # Test Case 18
        """Test the classify_triangle function with numbers near tolerance"""
        self.assertEqual(classify_triangle(0.0000011,
                                           0.0000012,
                                           0.00000123),
                         'Right Scalene Triangle', "Pythagoras Within 1%")
        self.assertEqual(classify_triangle(0.0001,
                                           0.0002,
                                           0.0002), 'Isosceles Triangle',
                         "Pythagoras Not within 1%")


if __name__ == '__main__':
    unittest.main(verbosity=2)
