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
    - Changing this to a separate function because sets are unordered
- Create an empty dictionary 
    - iterate through the letters in the set 
    - for each letter, count how many times it appears in the statement
    - assign that number as the value for each key from the set
- Return the dictionary
"""

def find_unique_letters(statement):
    unique_letters = list()
    for letter in statement: 
        if letter not in unique_letters and letter.isalpha():
            unique_letters.append(letter)
    return unique_letters

def count_letters(statement):
    unique_letters = find_unique_letters(statement)
    count_letters = dict()
    for letter in unique_letters:
        count_letters[letter] = statement.count(letter)
    return count_letters
    
print(count_letters(statement))

# Much easier method below:

def char_freq(statement):
    char_freq = {}
    statement = statement.replace(' ', '')
    for char in statement:
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq

print(char_freq(statement))