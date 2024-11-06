"""
Write a function that returns True if the string passed as an argument is a 
palindrome, False otherwise. A palindrome reads the same forwards and backwards. 
For this problem, the case matters and all characters matter.
"""

def is_palindrome(string):
    # print(string)
    # print(string[::-1])
    return string == string[::-1]

# # All of these examples should print True

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)

# # case matters
# print(is_palindrome('Madam') == False)

# # all characters matter
# print(is_palindrome("madam i'm adam") == False)

"""
1. Take string an remove any character that is not alphanumeric
2. Use .lower() to make the string lower 
3. Feed that into is_palindrome()
"""

def is_real_palindrome(string):
    new_string = ''
    for char in string:
        if char.isalnum() and char.isascii():
            new_string += char
    return is_palindrome(new_string.casefold())

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True