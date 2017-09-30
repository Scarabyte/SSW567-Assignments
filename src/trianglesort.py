#######################
#       SSW 567       #
#     Homework 05     #
#    Adam Burbidge    #
#######################
# Specify an upper limit for numbers to be "too big"
MAX_VALUE = 1000  # MAX_VALUE not defined in the requirements


def validate_inputs(number):
    """Verify that the given inputs are valid.

    Based on the requirements (Homework 04 Req 2.1), the inputs must be:
    1. Real numbers,
    2. Greater than 0, and
    3. "Not too big" (Note: poorly defined in the requirements)

    ("Too big" here is nominally defined as greater than 1000, but this
    can be changed if larger numbers are required.)
    """

    # Note: If we want to enforce the prospective numbers to be input
    # in a particular format, there are several RegEx strings we could use
    # to filter out invalid entries. (Some examples below that could be
    # used of modified for the allowable format.) For the sake of simplicity
    # in this function, however, we will assume that the "float" function is
    # sufficient to identify the numbers that we want to use.
    # Sample RegEx strings:
    # (-|\+)*\d*\.*\d+
    # (\+|-)*[0-9]+([.,][0-9]+)?
    # ([0-9]+)([\.,]?([0-9]+))?
    # ([\+-]?\.?)([0-9]+)([\.,]?([0-9]+))?
    # ([\+]?\d+[,]?\d+)|([-]?\d+[.]?\d+)|(\d+[.]?\d+)|([0-9]+)|(\.[0-9]+)
    # -?(?:[0-9]+(?:\.[0-9]*)?|(?:[0-9]+)?\.[0-9]+)

    try:
        testnumber = float(number)
        return (testnumber > 0 and testnumber <= MAX_VALUE)
    except ValueError:
        return False


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
    if validate_inputs(a) and validate_inputs(b) and validate_inputs(c):
        return max(a, b, c) <= a + b + c - max(a, b, c)
    else:
        return False


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

    In this implementation, a triangle may not have zero-length sides.

    Complex numbers, non-numeric input, and non-ASCII numbers are considered
    unsupported for this application, and will report an error.

    Likewise, the upper limit is not explicitly given in the requirements.
    The result will be given as 'Not A Triangle' if the numbers provided
    fail the input validation.

    Note: It may be preferable from a user's perspective to have separate
    error message(s) that indicate the exact reason for an input being rejected
    by the function, but the requirements did not specify how the error
    conditions were to be handled, only that an error be returned.
    """
    str_is_square = ''
    TOLERANCE = 0.01

    if is_triangle(a, b, c):
        mediannumber = sorted([a, b, c])[1]
        # Python 3 has the statistics module and median function, but
        # Python 2 doesn't so we just find it ourselves

        if (abs((min(a, b, c)**2.
                 + mediannumber**2.
                 - max(a, b, c)**2.)
                / max(a, b, c)**2.) <= TOLERANCE):
            str_is_square = 'Right '

        if a == b and b == c:
            # Equilateral triangle if all sides are of equal length
            return 'Equilateral Triangle'
        elif a == b or b == c or c == a:
            # Isosceles triangle if any two sides are of equal length
            return str_is_square + 'Isosceles Triangle'
        else:
            # Scalene triangles have no specific relationship between sides
            return str_is_square + 'Scalene Triangle'
    else:
        return 'Not A Triangle'
