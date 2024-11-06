# Use PEDAC, problem, examples, data structure, algorithm, code whenpossible

fruits = ("apple", "banana", "cherry", "date", "banana")

def count_item(collection, selection):
    count = 0
    for element in collection:
        if element == selection:
            count += 1
    return count
    
print(count_item(fruits, 'banana'))
print(fruits.count('banana'))

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a | b)

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

print(sum(ages.values()))
print(min(ages.values()))


statement = "The Flintstones Rock"

"""
Algorithm:
- Create a list of all the unique letters, case-sensitive, in the dictionary 
    - Create a set from the statement 
    - Change the set to a list 
- Create an empty dictionary 
    - iterate through the letters in the set 
    - for each letter, count how many times it appears in the statement
    - assign that number as the value for each key from the set
- Return the dictionary
"""

def count_letters(statement):
    list(set(statement)