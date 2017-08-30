#############################
#       SSW 567
#     Homework 01
#    Adam Burbidge
#############################
from math import sqrt


def isTriangle(a, b, c):
    """Check that the numbers form a valid triangle.

    Keyword arguments:
    a -- length of first side
    b -- length of second side
    c -- length of third side

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


def classifyTriangle(a, b, c):
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
    irrational) numbers. Since floating-point numbers generally cannot
    be represented exactly in binary notation, this function currently
    verifies the equation to an accuracy of 1E-07.
    """
    if isTriangle(a, b, c):
        # Python 3 has the statistics module and median function, but
        # Python 2 doesn't so we just find it ourselves
        mediannumber = sorted([a, b, c])[1]

        if a == b and b == c:
            # Equilateral triangle if all sides are of equal length
            return 'Equilateral'
        elif a == b or b == c or c == a:
            # Isosceles triangle if any two sides are of equal length
            if (abs(min(a, b, c)**2
                    + mediannumber**2
                    - max(a, b, c)**2) < 0.0000001):
                # Currently testing to an accuracy of 1E-07
                # This can be changed later if needed
                return 'IsoscelesRight'
            else:
                return 'Isosceles'
        else:
            # Scalene triangles have no specific relationship between sides
            if (abs(min(a, b, c)**2
                    + mediannumber**2
                    - max(a, b, c)**2) < 0.0000001):
                # Currently testing to an accuracy of 1E-07
                # This can be changed later if needed
                return 'ScaleneRight'
            else:
                return 'Scalene'
    else:
        return 'NotATriangle'


if __name__ == "__main__":
    print "isTriangle(3,4,5) = " + str(isTriangle(3, 4, 5))
    print "isTriangle(2,2,1) = " + str(isTriangle(2, 2, 1))

    print "isTriangle(1,4,6) = " + str(isTriangle(1, 4, 6))
    print "isTriangle(3,3,9) = " + str(isTriangle(3, 3, 9))

    print "classifyTriangle(3,4,5) = " + classifyTriangle(3, 4, 5)
    print "classifyTriangle(1,2,3) = " + classifyTriangle(1, 2, 3)
    print "classifyTriangle(1,1,sqrt(2) = " + classifyTriangle(1, 1, sqrt(2))