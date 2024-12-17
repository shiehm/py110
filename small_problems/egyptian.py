"""
Write two functions: 
- one that takes a Rational number as an argument, and returns a list of the 
  denominators that are part of an Egyptian Fraction representation of the number, 
- another that takes a list of numbers in the same format, and calculates the 
  resulting Rational number. 

Algorithm:
- Start with the largest unit fraction that is less than the argument 
    - Start with 1/1, then iterate the denominator up by 1 until something fits 
- Subtract it from the argument and store the remainder in a variable 
- Repeat this process until there is 0 left in the variable 
"""


from fractions import Fraction

def egyptian(fraction):
    results = []
    
    denominator = 1
    while Fraction(1, denominator) > fraction:
        denominator += 1
    
    remainder = fraction
    while remainder > 0:
        if Fraction(1, denominator) <= remainder:
            remainder -= Fraction(1, denominator)
            results.append(denominator)
        denominator += 1
    
    return results

# def unegyptian(denominators):
#     result = 0
#     for num in denominators:
#         result += Fraction(1, num)
#     return result

def unegyptian(denominators):
    return sum([Fraction(1, num) for num in denominators])

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))