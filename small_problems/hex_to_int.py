"""
Write a hexadecimal_to_integer function that converts a string representing a
hexadecimal number to its integer value. Hexadecimal numbers use base 16 
instead of 10, and the characters A, B, C, D, E and F 
(and the lowercase equivalents) correspond to decimal values of 10-15.

Requirements:
- Case doesn't matter, so just casefold, or upper assuming just US alphabet

First thing is to figure out how it actually works:
'4D9f' == 19871
4 = 4 x (16**3 = 4,096) = 16,384
D = 13 x (16**2 = 256) = 3,328
9 = 9 x (16**2 = 16) = 144
F = 15 x (16**0 = 1) = 15

So instead of multiplying by 10, you just multiply by 16 and add the last one
"""

def hexadecimal_to_integer(s):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    
    integer = 0
    for digit in s:
        integer = integer * 16 + DIGITS[digit.upper()]

    return integer


print(hexadecimal_to_integer('4D9f') == 19871)  # True