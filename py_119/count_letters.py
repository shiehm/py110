"""
Problem: 
Create a function that takes a string argument and returns a dict object in which the keys 
represent the lowercase letters in the string, and the values represent how often the 
corresponding letter occurs in the string.

Requirements:
- Character has to be lowercase and alphabetical (ignore the others)

Data Structure
I/O: string/dictionary

Algorithm
1. Loop:
    a. Create an empty dictionary to house the results 
    b. Iterating through each character in the string, assign dic[char] = string.count(char)
    c. Conditioned on if the character is lowercase and is alphabetical 
2. Return the dictionary result
"""

def count_letters(string):
    count_dic = {char: string.count(char) for char in string if char.isalpha() and char.islower()}
    return count_dic

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})