"""
Problem: Given a string of numeric digits, compute the greatest product of four consecutive digits in the string. 

Rules:
- The argument will always have more than 4 digits.

Data Structure:
- Input: String
- Output: Integer

Algorithm:
- Initialize empty list for consecutive_digits = []
- Find all possible products of 4 consecutive digits first 
    - Can create a list of all 4 length string-nums
        - for i in range(len(string) - 4)
        - consecutive_digits.append(string[i:i+4]
    - then a list of all the products of these string-nums
        - Initialize a products = []
        - Given a string turn it into a list
        - product = lst[0] * lst[1] * lst[2] * lst[3]
- Then find the highest max(product) and return it 
"""

def get_consecutives(string):
    consecutive = []
    for i in range(len(string) - (4-1)): # Key thing: If using iterator to get STARTING index, must add 1 to end param of range b/c of excl.
        digit = string[i:i+4]
        consecutive.append(digit)
    return consecutive 

def greatest_product(string):
    consecutive = get_consecutives(string)
    products = []
    for num in consecutive:
        lst = [int(digit) for digit in num]
        product = lst[0] * lst[1] * lst[2] * lst[3]
        products.append(product)
    return max(products)

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6