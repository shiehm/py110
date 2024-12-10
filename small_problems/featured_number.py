"""
A featured number (something unique to this exercise) is 
- an odd number that is 
- a multiple of 7, 
- with all of its digits occurring exactly once each. 

For example, 
- 49 is a featured number, 
- but 98 is not (it is not odd), 
- 97 is not (it is not a multiple of 7), 
- and 133 is not (the digit 3 appears twice).

Problem:
Write a function that takes an integer as an argument and returns the next 
featured number greater than the integer. Issue an error message if there 
is no next featured number. The largest possible featured number is 9876543201.

Input: integer
Output: integer representing the next greatest featured number or an error msg

Notes:
- We can breakdown each of these tests separately:
    - Is it odd
    - Is it a multiple of 7
    - Does each digit only appear once 
- We can choose one of these to iterate on, and test the other 2 factors

Algorithm: 
- Take the integer input, and find the next odd integer
- Test if this number is divisible by 7
    - If it is not, skip the next step 
- Test if this number's digits only appear once
    - If it satisfies this condition, return the number
    - If not, let the while loop continue 
    
"""
LARGEST = 9876543201
ERROR_MESSAGE = "There is no possible number that fulfills those requirements."

def is_divisible_7(num):
    return num % 7 == 0

def unique_digits(num):
    for digit in str(num):
        if str(num).count(digit) > 1:
            return False
    return True

def next_featured(num):
    start_num = num
    if start_num % 2 == 0:
        start_num += 1
    else:
        start_num += 2
    
    for next_num in range(start_num, LARGEST + 1, 2):
        if is_divisible_7(next_num) and unique_digits(next_num):
            return next_num
    
    return ERROR_MESSAGE

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True

print(next_featured(12))
print(next_featured(20))
print(next_featured(21))
print(next_featured(997))
print(next_featured(1029))
print(next_featured(999999))
print(next_featured(999999987))
print(next_featured(9876543186))
print(next_featured(9876543200))
print(next_featured(9876543201))

"""
Launch School Answer:
- What I like about this is that we know every other multiple of 7 is even
- So we can skip the even ones by iterating by 14
- Then we can start by finding the next ODD multiple of 7
- And add 14 to it
- Also the way it tests whether a digit is unique is much more pythonic

def to_odd_multiple_of_7(number):
    number += 1
    while number % 2 == 0 or number % 7 != 0:
        number += 1

    return number

def all_unique(number):
    digits = list(str(number))
    return len(digits) == len(set(digits))

def next_featured(number):
    MAX_FEATURED = 9876543201
    featured_num = to_odd_multiple_of_7(number)

    while featured_num <= MAX_FEATURED:
        if all_unique(featured_num):
            return featured_num

        featured_num += 14

    return "There is no possible number that fulfills those requirements."
"""

# Reworked the LS answer below:

def next_odd_multiple_7(num):
    num += 1
    while num % 2 == 0 or num % 7 != 0:
        num += 1
    return num

def has_unique_digits(num):
    str_num = list(str(num))
    return len(str_num) == len(set(str_num))

def ls_next_featured(num):
    MAX_FEATURED = 9876543201
    next_num = next_odd_multiple_7(num)
    while next_num <= MAX_FEATURED:
        if has_unique_digits(next_num):
            return next_num
        next_num += 14

    return "There is no possible number that fulfills those requirements."

print(ls_next_featured(12) == 21)                  # True
print(ls_next_featured(20) == 21)                  # True
print(ls_next_featured(21) == 35)                  # True
print(ls_next_featured(997) == 1029)               # True
print(ls_next_featured(1029) == 1043)              # True
print(ls_next_featured(999999) == 1023547)         # True
print(ls_next_featured(999999987) == 1023456987)   # True
print(ls_next_featured(9876543186) == 9876543201)  # True
print(ls_next_featured(9876543200) == 9876543201)  # True
print(ls_next_featured(9876543201) == error)       # True