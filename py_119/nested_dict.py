"""
1. We need to access the dictionary value of the key names in the outer dictionary
2. Then the age key in the innder dictionary
3. And then only sum up those that are male

Expression for Value in Collection if Condition
"""
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

ages = [munsters[name]['age'] for name in munsters if munsters[name]['gender'] == 'male']
sum(ages)

total = 0
for name in munsters: 
    if munsters[name]['gender'] == 'male':
        total += munsters[name]['age']

print(total)

"""
Dictionary Comprehensions
"""

# Can extract the dict comprehension to a function
lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

[{k: v + 1 for k, v in dic.items()} for dic in lst]

def increment(dic):
    return {k: v + 1 for k, v in dic.items()}

[increment(dic) for dic in lst]