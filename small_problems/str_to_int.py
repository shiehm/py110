"""
Problem:
Write a function that takes a string of digits and returns the appropriate 
number as an integer. You may not use any of the standard conversion functions 
available in Python, such as int. Your function should calculate the result 
by using the characters in the string.

Explicit Requirements:
- No use of int() or standard conversion functions 
- For now, do not worry about leading + or - signs, 
- nor should you worry about invalid characters; 
- assume all characters are numeric.

Input: String of numbers
Output: Integer

Algoritm: 
- Go character by character starting from digits place
- Use ord() to turn the character into unicode which is int
- Unicode for 0-9 runs from 48-57, so subtract 48
- For each tens place, multiply by 10, 100, etc. 
- Save each number into a variable using augmented assignment
- Add up all the numbers in the list
"""

def string_to_integer(string):
    digits_places = len(string)
    integer = 0
    for i in range(1, digits_places + 1):
        integer += (ord(string[-i]) - 48) * (10**(i - 1))
    return integer

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True


"""
This one is the better solution since it doesn't use a built in function
Whereas mine uses len() and ord()
"""

def string_to_integers(s):
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
        '9': 9
    }
    
    integer = 0
    for digit in s:
        integer = integer * 10 + DIGITS[digit]

    return integer

print(string_to_integers("4321") == 4321)  # True
print(string_to_integers("570") == 570)    # True

"""
This one's even more elegant using a dict constructor, though it uses str()

def string_to_integer(string):

    result = 0
    dict_string = {str(num): num for num in range(0, 10)} 

    for num in string:
        int_num = dict_string[num]
        result = (10 * result) + int_num

    return result    
    
"""


# Adding signs to it:
"""
The string may have a leading + or - sign; if the first character is a +, 
your function should return a positive number; if it is a -, your function 
should return a negative number. If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python, 
such as int. You may, however, use the string_to_integer function from the previous exercise.
"""

def string_to_signed_integer(string):
    if string[0] == '+':
        return string_to_integers(string[1:])
    elif string[0] == '-':
        return -string_to_integers(string[1:])
    else:
        return string_to_integers(string)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

"""
Using match-case (doesn't work on amazon cloud9 python 3.9):

def string_to_signed_integer(string):
    match string[0]:
        case '-':
            return -string_to_integer(string[1:])
        case '+':
            return string_to_integer(string[1:])
        case _:
            return string_to_integer(string)
"""