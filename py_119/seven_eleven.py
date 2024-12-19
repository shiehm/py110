"""
Problem:
Given a single integer, find the sum of all the multiples of 7 or 11 that are less than the argument. 

Rules:
- If a number is a multiple of both 7 and 11, count it just once.
- If the argument is negative, return 0. (range will not produce an iterable). 
- Assuming it's < not <= the argument 

Examples:
- For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.

Data Structure:
- Can use sets and range to get the multiples of 7 and 11 that are below the integer 


Algorithm:
- First determine:
    - All the multiples of 7 below the integer --> range(7, integer, 7)
    - All the multiples of 11 below the integer --> range(11, integer, 11)
    - Use a set([*7s, *11s]) to get total multiples
- return len(multiples)
"""

def seven_eleven(num):
    seven = list(range(7, num, 7))
    eleven = list(range(11, num, 11))
    multiples = set([*seven, *eleven]) # can also do set(seven + eleven)
    return sum(multiples)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)