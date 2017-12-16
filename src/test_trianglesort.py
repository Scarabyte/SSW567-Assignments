#######################
#       SSW 567       #
#     Homework 05     #
#    Adam Burbidge    #
#######################
import unittest
import random
import math
from trianglesort import *  # pylint: disable=wildcard-import
# Note: Ignoring the wildcard import in PyLint because we do want to exercise
# every function in the module and be warned if there are any unused ones.


class TestValidateInputs(unittest.TestCase):
    """This class tests the validate_inputs function"""

    def setUp(self):
        random.seed()

    def test_validate_inputs_valid_value(self):
        """Test input validation with a valid value"""
        # We'll choose a random number since any number
        # in the valid range should work
        # Since random.uniform returns a value in the range [a, b)
        # use a slight mathematical hack to generate range (a, b]
        # ANY number in this range should pass validation,
        # so in theory we should be able to randomly select any number.
        # (Note that the probability of returning exactly MAX_VALUE
        # or exactly 0 is effectively zero anyway.)
        testnumber = -random.uniform(-MAX_VALUE, 0)
        self.assertTrue(validate_inputs(testnumber),
                        "Result with " + str(testnumber))

    def test_validate_inputs_upper_limit(self):
        """Test input validation at the upper limit"""
        self.assertTrue(validate_inputs(MAX_VALUE))

    def test_validate_inputs_lower_limit(self):
        """Test input validation at the lower limit"""
        self.assertFalse(validate_inputs(0), "0 should be disallowed")

    def test_validate_inputs_below_lower_limit(self):
        """Test input validation below the lower limit"""
        testnumber = -random.uniform(0, MAX_VALUE)
        # There is nothing "special" about -MAX_VALUE in the lower range,
        # but it was a convenient stopping point for the random range.
        self.assertFalse(validate_inputs(testnumber))

    def test_validate_inputs_above_upper_limit(self):
        """Test input validation above the upper limit"""
        testnumber = random.uniform(MAX_VALUE, 2 * MAX_VALUE)
        # There is nothing "special" about 2 * MAX_VALUE in the upper range,
        # but it was a convenient stopping point for the random range.
        self.assertFalse(validate_inputs(testnumber))

# Original test cases follow.

# Original test case, still used for the Invalid Input equivalence class
# (rather than creating a new test, since we already had this one)
    def test_validate_inputs_NonNumeric(self):
        # Test Case 04
        """Verify that non-numeric inputs fail validation"""
        self.assertFalse(validate_inputs("555.123.4567"))
        self.assertFalse(validate_inputs("5i+3j"))
        self.assertFalse(validate_inputs("ABCD"))
        self.assertFalse(validate_inputs("+1-(800)-555-2468"))


class TestIsTriangle(unittest.TestCase):
    """This class tests the is_triangle function"""

    def setUp(self):
        pass

    def test_is_triangle_true_valid_inputs_first_smallest(self):
        """Verify valid inputs that form a triangle, first input smallest"""
        self.assertTrue(is_triangle(3, 4, 5))

    def test_is_triangle_true_valid_inputs_second_smallest(self):
        """Verify valid inputs that form a triangle, second input smallest"""
        self.assertTrue(is_triangle(7, 2, 8))

    def test_is_triangle_true_valid_inputs_third_smallest(self):
        """Verify valid inputs that form a triangle, third input smallest"""
        self.assertTrue(is_triangle(4, 3, 1))

    def test_is_triangle_two_inputs_equal_third(self):
        """Verify valid inputs where the sum of two values equals the third
        Note that the requirements were unclear as to whether or not we should
        accept this as a valid triangle, but if we do it would be a triangle
        with zero area."""
        self.assertTrue(is_triangle(3, 1, 4))

    def test_is_triangle_false_valid_inputs_first_smallest(self):
        """Verify valid inputs that don't form a triangle, first smallest"""
        self.assertFalse(is_triangle(1, 2, 4))

    def test_is_triangle_false_valid_inputs_second_smallest(self):
        """Verify valid inputs that don't form a triangle, second smallest"""
        self.assertFalse(is_triangle(8, 3, 12))

    def test_is_triangle_false_valid_inputs_third_smallest(self):
        """Verify valid inputs that don't form a triangle, third smallest"""
        self.assertFalse(is_triangle(9, 5, 2))

    def test_is_triangle_false_first_input_invalid(self):
        """Verify that is_triangle fails if first input is invalid"""
        self.assertFalse(is_triangle(-3, 4, 5))

    def test_is_triangle_false_second_input_invalid(self):
        """Verify that is_triangle fails if second input is invalid"""
        self.assertFalse(is_triangle(3, "ABCD", 5))

    def test_is_triangle_false_third_input_invalid(self):
        """Verify that is_triangle fails if third input is invalid"""
        self.assertFalse(is_triangle(3, 4, "3i+4j"))


class TestClassifyTriangle(unittest.TestCase):
    """This class tests the classify_triangle function"""

    def setUp(self):
        pass

    def test_classify_triangle_first_input_invalid(self):
        """Verify classify_triangle returns error when first input invalid"""
        self.assertEqual(classify_triangle('hello', 1, 1), 'Not A Triangle')

    def test_classify_triangle_second_input_invalid(self):
        """Verify classify_triangle returns error when second input invalid"""
        self.assertEqual(classify_triangle(5, -4, 3), 'Not A Triangle')

    def test_classify_triangle_third_input_invalid(self):
        """Verify classify_triangle returns error when third input invalid"""
        self.assertEqual(classify_triangle(5, 4, 0), 'Not A Triangle')

    def test_classify_triangle_non_triangle(self):
        """Verify inputs that pass validation but don't form a triangle"""
        self.assertEqual(classify_triangle(1, 3, 1), 'Not A Triangle')
        self.assertEqual(classify_triangle(1, 4, 6), 'Not A Triangle')

    def test_classify_triangle_equilateral_integer(self):
        """Verify an equilateral triangle with integer side lengths"""
        self.assertEqual(classify_triangle(3, 3, 3),
                         'Equilateral Triangle')

    def test_classify_triangle_equilateral_float(self):
        """Verify an equilateral triangle with flaoting point side lengths"""
        self.assertEqual(classify_triangle(3.5, 3.5, 3.5),
                         'Equilateral Triangle')

    def test_classify_triangle_isosceles_regular(self):
        """Verify an isosceles triangle"""
        self.assertEqual(classify_triangle(2, 3, 2),
                         'Isosceles Triangle')

    def test_classify_triangle_isosceles_right(self):
        """Verify an isosceles triangle"""
        self.assertEqual(classify_triangle(2, 2.828, 2),
                         'Right Isosceles Triangle')
        self.assertEqual(classify_triangle(math.sqrt(2), math.sqrt(2), 2),
                         'Right Isosceles Triangle')

    def test_classify_triangle_scalene_regular(self):
        """Verify an isosceles triangle"""
        self.assertEqual(classify_triangle(7, 4.2, 3), 'Scalene Triangle')
        self.assertEqual(classify_triangle(1, 2, 3), 'Scalene Triangle')
        self.assertEqual(classify_triangle(2.5, 3.4, 5.1), 'Scalene Triangle')

    def test_classify_triangle_scalene_right(self):
        """Verify an isosceles triangle"""
        self.assertEqual(classify_triangle(3, 5, 4), 'Right Scalene Triangle')
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene Triangle')

    def test_classify_triangle_within_tolerance(self):
        """Test a right triangle with sides within 1%"""
        side_1, side_2 = 2, 2
        side_3 = math.sqrt((side_1**2 + side_2**2)
                           * (1 - TOLERANCE + 0.1 * TOLERANCE))
        self.assertEqual(classify_triangle(side_1, side_2, side_3),
                         'Right Isosceles Triangle')

    def test_classify_triangle_out_of_tolerance(self):
        """Test a right triangle with sides more than 1% different"""
        side_1, side_2 = 2, 2
        side_3 = math.sqrt((side_1**2 + side_2**2) * 0.989)
        self.assertEqual(classify_triangle(side_1, side_2, side_3),
                         'Isosceles Triangle')

# Original test cases follow

# Partially obsolete because it is replaced by
# test_classify_triangle_scalene_regular
# But we do not have another test case for non-integer non-triangles
    def test_classify_triangle_non_integer_numbers(self):
        # Test Case 13
        """Test some triangles that do not have integer-length sides"""
        self.assertEqual(classify_triangle(2.5, 3.4, 7.6), 'Not A Triangle')
        self.assertEqual(classify_triangle(2.5, 3.4, 5.1), 'Scalene Triangle')

# Original test case still useful because I don't have one that
# explicitly checks for zero-length sides, although it
# could be combined with
# test_classify_triangle_first_input_invalid
# test_classify_triangle_second_input_invalid
# test_classify_triangle_third_input_invalid
    def test_classify_triangle_zero(self):
        # Test Case 14
        """Test the classify_triangle function with zero-length sides"""
        self.assertEqual(classify_triangle(3, 0, 5), 'Not A Triangle')
        self.assertEqual(classify_triangle(0, 123, 0), 'Not A Triangle')
        self.assertEqual(classify_triangle(5.23461, 0, 0), 'Not A Triangle')

# Original test case still useful because I don't have one that
# explicitly checks for negative-length sides, although it
# could be combined with
# test_classify_triangle_first_input_invalid
# test_classify_triangle_second_input_invalid
# test_classify_triangle_third_input_invalid
    def test_classify_triangle_negative_numbers(self):
        # Test Case 15
        """Test the classify_triangle function with some negative numbers"""
        self.assertEqual(classify_triangle(-1, 123, 3.14), 'Not A Triangle')
        self.assertEqual(classify_triangle(1, -123, 300), 'Not A Triangle')

# Could be combined, as applicable, with
# test_classify_triangle_scalene_right
# test_classify_triangle_equilateral_float
# test_classify_triangle_non_triangle
# (But better to use trianglesort.TOLERANCE so it will adapt to changes)
    def test_classify_triangle_big_numbers(self):
        # Test Case 16
        """Test the classify_triangle function with "big" numbers"""
        self.assertEqual(classify_triangle(1000, 999, 10),
                         'Right Scalene Triangle')
        # These values are within 1% in the Pythagorean equation

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

# Could be combined with
# test_classify_triangle_non_triangle
# test_classify_triangle_isosceles_regular
# test_classify_triangle_equilateral_float
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

# Could be combined with
# test_classify_triangle_within_tolerance
# test_classify_triangle_out_of_tolerance
# (But better to use trianglesort.TOLERANCE so it will adapt to changes)
    def test_classify_triangle_tolerance(self):
        # Test Case 18
        """Test the classify_triangle function with numbers near tolerance"""
        self.assertEqual(classify_triangle(0.00011,
                                           0.00012,
                                           0.000162),
                         'Right Scalene Triangle')  # Pythagoras Within 1%
        self.assertEqual(classify_triangle(0.0001,
                                           0.0002,
                                           0.0001),
                         'Isosceles Triangle')  # Pythagoras Not within 1%


if __name__ == '__main__':
    unittest.main(verbosity=2)
