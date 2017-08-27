#############################
#       SSW 567
#     Homework 01
#    Adam Burbidge
#############################


def isTriangle(a,b,c):
    """Check that the numbers form a valid triangle.
    
    In order for three numbers (representing the lengths of line segments)
    to form a triangle, the sum of the two smaller numbers must be
    greater than or equal to the largest number.
    
    This can be seen in the Triangle Inequality:
    
        a + b >= c
        a + c >= b
        b + c >= a
    
    or, writing it in a way that can be easily implemented in this function,
    
        max(a,b,c) <= a + b + c - max(a,b,c)    
    
    (Note that equality only occurs in the case of a triangle with zero area,
    which effectively forms a straight line with one 180 and two 0 degree angles,
    thereby demonstrating that the shortest distance between two points is a
    straight line in Euclidean space.)
    
    See https://en.wikipedia.org/wiki/Triangle_inequality 
    for a more detailed explanation, and mathematical proofs at
    https://proofwiki.org/wiki/Triangle_Inequality
    https://proofwiki.org/wiki/Sum_of_Two_Sides_of_Triangle_Greater_than_Third_Side
    """
    return max(a,b,c) <= a + b + c - max(a,b,c)

def classifyTriangle(a,b,c):
    pass

if __name__ == "__main__":
    print "isTriangle(3,4,5) = " + str(isTriangle(3,4,5))
    print "isTriangle(2,2,1) = " + str(isTriangle(2,2,1))
    
    print "isTriangle(1,4,6) = " + str(isTriangle(1,4,6))
    print "isTriangle(3,3,9) = " + str(isTriangle(3,3,9))
