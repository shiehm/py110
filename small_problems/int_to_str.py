"""
Problem: Write a function that converts a non-negative integer value 
(e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

Requirements:
- Can't use standard conversion functions available in Python, such as str
- Your function should construct the string by analyzing and manipulating the number.

Input: Int
Output: Str

Algorithm:
1. Create a dictionary of mappings to map int to str, using dict comprehension
2. Get the number of places, which will be used to get the base-10 quotients sans remainders
3. Iterate through the powers of 10 starting from the last (leftmost digit place)
    a. Get the quotient sans remainder and add it to the string
    b. Use the remainder for the next operation
4. Return the saved new string

Need an integer digits counter:
1. Using a while loop, // 10 and + 1 to counter until its 0 
2. Add if num == 0, then it's 1 digit long
"""

def digits_counter(num):
    if num == 0:
        return 1
    
    counter = 0
    while num > 0:
        num = num // 10
        counter += 1
    return counter

def integer_to_string(num):
    NUM_DICT = {x: f'{x}' for x in range(10)}

    digits = digits_counter(num)
    num_str = ''
    remainder = num
    
    for i in range(digits - 1, -1, -1):
        div_mod = divmod(remainder, 10**i)
        digit = div_mod[0]
        num_str += NUM_DICT[digit]
        remainder = div_mod[1]
    return num_str

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

"""
The solution was far more elegant than what I made above, 
by setting the number = to the quotient.


DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return result or '0'
"""

def signed_integer_to_string(num):
    if num == 0:
        return '0'
    elif abs(num) == num:
        return '+' + integer_to_string(num)
    else: 
        return '-' + integer_to_string(abs(num))

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True