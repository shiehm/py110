munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

age = 0
for key, value in munsters.items():
    if value['gender'] == 'male':
        age += value['age']

sum([value['age'] for key, value in munsters.items() if value['gender'] == 'male'])

"""
Dictionary Comprehensions. 
"""

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

{k: v for k, v in lst}
{item[0]: item[1] for item in lst}

"""
Sum odds 
"""

def odd_total(lst):
    return sum([num for num in lst if num % 2 != 0])

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

sorted(lst, key=odd_total)

"""
More Dict Comprehensions
"""

lst = [
    {'a': 1}, 
    {'b': 2, 'c': 3}, 
    {'d': 4, 'e': 5, 'f': 6}
]

new_lst = []
for dic in lst:
    new_lst.append({k: v + 1 for k, v in dic.items()})

[{k: v + 1 for k, v in dic.items()} for dic in lst]

"""
Nested Lists
"""

lst = [
    [2], 
    [3, 5, 7, 12], 
    [9], 
    [11, 15, 18]
]

new_lst = []
for sub_lst in lst:
    new_sub_lst = []
    for num in sub_lst:
        if num % 3 == 0:
            new_sub_lst.append(num)
    new_lst.append(new_sub_lst)

new_lst

[[num for num in sub_lst if num % 3 == 0] for sub_lst in lst]

"""
Selection with nested ditcionary comprehension
"""


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
for key, value in dict1.items():
    if value['type'] == 'fruit':
       new_lst.append([color.capitalize() for color in value['colors']])
    elif value['type'] == 'vegetable':
        new_lst.append(value['size'].upper())

[[color.capitalize() for color in value['colors'] if value['type'] == 'fruit'] for key, value in dict1.items()]


"""
Transformations with dictionaries
"""

def transform_item(value):
    if value['type'] == 'fruit':
       return [color.capitalize() for color in value['colors']]
    elif value['type'] == 'vegetable':
        return value['size'].upper()

[transform_item(value) for key, value in dict1.items()]

"""
Given the following data structure, write some code to return a list 
that contains only the dictionaries where all the numbers are even. 
"""

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# Create a helper function to see if all the numbers in a list are even:
def lst_is_even(lst):
    results = [num % 2 == 0 for num in lst]
    return all(results)

def dic_is_even(dic):
    results = [lst_is_even(values) for key, values in dic.items()]
    return all(results)

new_lst = [dic for dic in lst if dic_is_even(dic)]
print(new_lst)

def dic_is_even(dic):
    results = []
    for key, values in dic.items(): 
        results.append(lst_is_even(values))
    return all(results)

new_lst = []
for dic in lst:
    if dic_is_even(dic):
        new_lst.append(dic)

print(new_lst) # [{e: [8], f: [6, 10]}]

"""
The following dictionary has list values that contains strings. 
Write some code to create a list of every vowel (a, e, i, o, u) 
that appears in the contained strings, then print it.
"""

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

VOWELS = 'aeiou'
vowels_only = ''

for key, value in dict1.items():
    for word in value:
        for char in word:
            if char in VOWELS or char in VOWELS.upper():
                vowels_only += char

list_of_vowels = list(vowels_only)
print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

[char 
     for key, value in dict1.items()
     for word in value
     for char in word
     if char in VOWELS or char in VOWELS.upper()
]