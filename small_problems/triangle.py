"""
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.

To be a valid triangle, the sum of the lengths of the two shortest sides 
must be greater than the length of the longest side, and every side must 
have a length greater than 0. If either of these conditions is not satisfied, 
the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as 
arguments and returns one of the following four strings representing the 
triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.
"""

def valid_triange(side1, side2, side3):
    sorted_sides = sorted([side1, side2, side3])
    if 0 in sorted_sides:
        return False
    elif sum(sorted_sides[:2]) <= sorted_sides[2]:
        return False
    else:
        return True

def triangle(side1, side2, side3):
    if not valid_triange(side1, side2, side3):
        return 'invalid'
    
    sorted_sides = sorted([side1, side2, side3])
    counts = [sorted_sides.count(side1), sorted_sides.count(side2), sorted_sides.count(side3)]
    if 3 in counts:
        return 'equilateral'
    elif 2 in counts:
        return 'isosceles'
    else:
        return 'scalene'

print(triangle(3, 3, 3))
print(triangle(3, 3, 1.5))
print(triangle(3, 4, 5))
print(triangle(0, 3, 3))
print(triangle(3, 1, 1))

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True