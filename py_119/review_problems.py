"""
Problem: extract all the vowels from the lists in the values of the dictionary and print it 
    Input: string
    Output: string
    Requirements:
    - Explicit
    - Implicit 

Examples / Test Cases: provided
Data Structure: Since strings are harder to work with and iterate through, use a list so we can use list comprehensions as an intermediate data structure

Algorithm:
Starting from the bottom up. Thinkin about what I need to iterate over from the lowest level up
1. Create a function that extracts all the vowels from a string and returns it as a string
2. Create a function that extracts all the vowels in a list of strings and returns it as a string
3. Iterate through the dictionary values which are lists and extract all the vowels as a string

OR
1. Extract all words in the values to one list
    - Iterate through the dictionary values, and inner itearate through the words
    - Append each word to a comprehensive list 
2. Iterate through each word 
    - For every word iterate through the characters and append the vowels to a new list
3. Return the new list joined into a string
"""

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

def extract_vowels_string(string):
    str_lst = list(string)
    vowels = [char for char in str_lst if char.lower() in 'aeiou']
    return ''.join(vowels)

def extract_vowels_list(lst):
    vowels = [extract_vowels_string(word) for word in lst]
    return ''.join(vowels)

def extract_vowels_dict(dic):
    vowels = [extract_vowels_list(lst) for lst in dic.values()]
    joined = ''.join(vowels)
    return list(joined)

extract_vowels_dict(dict1)

# List comprehension solution with good formatting making it clear
[
    char for key in dict1 
         for word in dict1[key]
         for char in word
         if char in 'aeiou'
]



"""
Problem: Return a list with only dictionaries where all numbers are even

Data Structure: 
    i/o: list of dictionaries

Algorithm:
1. Check if all the values in a dictionary are even
2. Create a new list with only the dictionaries where all values are even 
"""

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def check_evens(dic):
    for nums in dic.values():
        return all([num % 2 == 0 for num in nums])

[dic for dic in lst if check_evens(dic)]



# We want for color of the fruits capitalized and the size of the vegetables in caps

# Outer Dictionary - dict1
    # Innter Dictionary - fruits or vegetable dictionaries
        # string
        # list <-- access this
        # string <-- access this

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

new_lst = []
for item in dict1:
    if dict1[item]['type'] == 'fruit':
        new_lst.append([color.capitalize() for color in dict1[item]['colors']])
    elif dict1[item]['type'] == 'vegetable':
        new_lst.append(dict1[item]['size'].upper())

def transform(item):
    if dict1[item]['type'] == 'fruit':
        return [color.capitalize() for color in dict1[item]['colors']]
    elif dict1[item]['type'] == 'vegetable':
        return dict1[item]['size'].upper()

[transform(item) for item in dict1]



"""
Sort the lists by their string value
"""

# Sorted function with key parameter

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

[sorted(str(element) for element in sub_lst) for sub_lst in lst]
[sorted(sub_lst, key=str) for sub_lst in lst]