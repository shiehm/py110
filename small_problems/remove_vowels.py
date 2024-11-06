"""
Problems: Write a function that takes a list of strings and returns a list 
of the same string values, but with all vowels (a, e, i, o, u) removed.

Input: List of strings
Output: List of strings

Algortihm:
1. Create a global VOWELS constant list
2. Create a new list
3. Iterate through the strings in the lists
4. Create a new string. 
5. Iterate through the characters in the string
6. Add the char to new string if its not in VOWELS
7. Append the string to the new list
8. Return the new list
"""

def remove_vowels(lst):
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    new_lst = []
    for string in lst:
        new_string = ''
        for char in string:
            if char not in VOWELS:
                new_string += char
        new_lst.append(new_string)
    return new_lst


"""
Trying the LS solution way, with 2 functions:
- One to strip vowels from a string
- One to repeat that for a list

Algorithm:
- Strip vowels from string:
1. Create a variable to hold all the vowels lower and upper 
2. Take the string as an argument, iterate over its characters
3. Keep the character only if it is not in vowels 
4. Return this string

- Strip vowels from list of strings:
1. Iterate through the strings in the list
2. Apply the strip_vowels function to each
3. Return the list
"""

def strip_vowels(string):
    VOWELS = 'aeiouAEIOU'
    new_string = [char for char in string if char not in VOWELS]
    return ''.join(new_string)

def remove_vowels(lst):
    return [strip_vowels(string) for string in lst]


# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True