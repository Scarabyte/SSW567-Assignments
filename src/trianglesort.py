#######################
#       SSW 567       #
#     Homework 04     #
#    Adam Burbidge    #
#######################
from math import sqrt


def is_triangle(a, b, c):
    """Check that the numbers form a valid triangle.

    Keyword arguments:
    a -- length of first side
    b -- length of second side
    c -- length of third side

    The inputs do not have to be sorted in ascending order.

    In order for three numbers (representing the lengths of line segments)
    to form a triangle, the sum of the two smaller numbers must be
    greater than or equal to the largest number.

    This can be seen in the Triangle Inequality:

        a + b >= c
        a + c >= b
        b + c >= a

    or, writing it in a way that can be easily implemented in this function,

        max(a, b, c) <= a + b + c - max(a, b, c)

    (Note that equality only occurs in the case of a triangle with zero area,
    which effectively forms a straight line, or a triangle with one 180 and
    two 0 degree angles, thereby demonstrating that the shortest distance
    between two points is a straight line in Euclidean space.)

    See https://en.wikipedia.org/wiki/Triangle_inequality
    for a more detailed explanation, and mathematical proofs at
    https://proofwiki.org/wiki/Triangle_Inequality
    https://proofwiki.org/wiki/Sum_of_Two_Sides_of_Triangle_Greater_than_Third_Side
    """
    return max(a, b, c) <= a + b + c - max(a, b, c)


def classify_triangle(a, b, c):
    """Classify triangles based on their side lengths.

    Keyword arguments:
    a -- length of first side
    b -- length of second side
    c -- length of third side

    There are three types of triangles:

    - Equilateral triangles have three sides of equal length
    - Isosceles triangles have two sides of equal length
    - Scalene triangles have all three sides of different lengths

    In addition, a Scalene or Isosceles triangle may also form a right triangle
    where one of the angles is 90 degrees and the sides of the triangle
    satisfy the Pythagorean theorem:

        a**2 + b**2 = c**2

    Note that most solutions will involve floating-point (and often
    irrational) numbers. Since floating-point numbers in general cannot
    be represented exactly in binary notation, this function currently
    verifies the equation with a tolerance of 1E-07.

    Complex numbers, non-numeric input, and non-ASCII numbers are considered
    unsupported for this application, and may yield unexpected results.

    Likewise, the upper limit is nominally stated as 1E+07.
    This is not explicitly enforced, and so larger numbers may succeed,
    but the accuracy of results is not guaranteed; the user assumes
    responsibility for testing numbers outside the stated range.
    """
    TOLERANCE = 0.0000001
    # Currently testing to an accuracy of 1E-07
    # This can be changed later if needed

    if is_triangle(a, b, c):
        # Python 3 has the statistics module and median function, but
        # Python 2 doesn't so we just find it ourselves
        mediannumber = sorted([a, b, c])[1]

        if a == b and b == c:
            # Equilateral triangle if all sides are of equal length
            return 'Equilateral Triangle'
        elif a == b or b == c or c == a:
            # Isosceles triangle if any two sides are of equal length
            if (abs(min(a, b, c)**2
                    + mediannumber**2
                    - max(a, b, c)**2) < TOLERANCE):
                return 'Right Isosceles Triangle'
            else:
                return 'Isosceles Triangle'
        else:
            # Scalene triangles have no specific relationship between sides
            if (abs(min(a, b, c)**2
                    + mediannumber**2
                    - max(a, b, c)**2) < TOLERANCE):
                return 'Right Scalene Triangle'
            else:
                return 'Scalene Triangle'
    else:
        return 'Not A Triangle'


if __name__ == "__main__":
    print "is_triangle(3,4,5) = " + str(is_triangle(3, 4, 5))
    print "is_triangle(2,2,1) = " + str(is_triangle(2, 2, 1))
    print "is_triangle(10,10,10) = " + str(is_triangle(10, 10, 10))

    print "is_triangle(1,4,6) = " + str(is_triangle(1, 4, 6))
    print "is_triangle(3,3,9) = " + str(is_triangle(3, 3, 9))

    print
    print "Show examples of every valid classification"
    print "classify_triangle(5,3,4) = " + classify_triangle(5, 3, 4)
    print "classify_triangle(2,1,3) = " + classify_triangle(2, 1, 3)
    print ("classify_triangle(1,1,sqrt(2)) = "
           + classify_triangle(1, 1, sqrt(2)))
    print "classify_triangle(2,2,1) = " + classify_triangle(2, 2, 1)
    print "classify_triangle(3,3,3) = " + classify_triangle(3, 3, 3)

    print
    print "Show inputs which fail the Triangle Inequality are not triangles"
    print "classify_triangle(3,4,6) = " + classify_triangle(3, 4, 6)
    print "classify_triangle(3,4,7) = " + classify_triangle(3, 4, 7)
    print "classify_triangle(3,4,8) = " + classify_triangle(3, 4, 8)

    print
    print "Negative numbers are considered 'NotATriangle'"
    print "classify_triangle(-3,4,5) = " + classify_triangle(-3, 4, 5)
    print "classify_triangle(3,-4,5) = " + classify_triangle(3, -4, 5)
    print "classify_triangle(3,4,-5) = " + classify_triangle(3, 4, -5)
    print "classify_triangle(-3,-4,5) = " + classify_triangle(-3, -4, 5)
    print "classify_triangle(-3,-4,-5) = " + classify_triangle(-3, -4, -5)
    print "classify_triangle(-5,-5,-5) = " + classify_triangle(-5, -5, -5)

    print
    print "Demonstrate non-integer numbers"
    print ("classify_triangle(2.5, 3.4, 7.6) = "
           + classify_triangle(2.5, 3.4, 7.6))
    print ("classify_triangle(2.5, 3.4, 5.1) = "
           + classify_triangle(2.5, 3.4, 5.1))

    print
    print "Demonstrate irrational numbers"
    print ("classify_triangle(1/sqrt(2),1/sqrt(2),1) = "
           + classify_triangle(1 / sqrt(2), 1 / sqrt(2), 1))
    print ("classify_triangle(1/sqrt(2),1/sqrt(2),2) = "
           + classify_triangle(1 / sqrt(2), 1 / sqrt(2), 2))

    print
    print "Demonstrate triangles with one or more zero-length sides"
    print "classify_triangle(1,2,0) = " + classify_triangle(1, 2, 0)
    print "classify_triangle(2,2,0) = " + classify_triangle(2, 0, 2)
    print "classify_triangle(2,0,0) = " + classify_triangle(2, 0, 0)
