"""
Problem:

Given a list of strings, return a new list where the strings are sorted based on 
the highest number of adjacent consonants a string contains. If two strings 
contain the same highest number of adjacent consonants, they should retain their 
original order in relation to each other. Consonants are considered adjacent if 
they are next to each other in the same word or if there is a space between two 
consonants in adjacent words.

Input: list of strings
Output: list of strings, sorted

Explicit Requirements:
- If 2 strings are tied for the amount of adjacent consonants, keep original order
- Adjacency is defined as being next to each other or separated by a space

Implicit Requirements:
- There can be multiple words

Questions:
- Are all the characters alpha? Or are there numbers, special char, etc. [All alpha in examples]
- Does it matter if we return the same object or a new object? [N/A]
- Do the words have to be valid words? [No]
- Will there always be multiple words in the same string? [No]
- What is the sort order? Assuming descending. [Sort in descending with highest first]
- Does case matter? [All examples are lower case]
- What if there is only 1 consonant? [Doesn't matter, don't count it]
- What if there are multiple spaces? [Examples don't clarify]

Examples / Test Cases: See examples below 

Data Structures: Return a sorted list, could be a dictionary 

Notes:
- We need a way of differentiating consonants vs. non-consonants (i.e. vowels)
- We can create a list of vowels and test if a character isalpha() and not in vowels
- We can use indexing to compare with the character before or after


Algorithm:
1. Create an is_consonant() function. 
    a. Declare a list of vowels to exclude from a isaplha() test
    b. Take in a character as an argument, and return True if consonant 
2. Create a num_adj_consonants() function. 
    a. Declare a adjacent consonants counter
    b. Pass in a string and remove all whitespaces 
    c. Test if it is at least 2 characters long, if not return 0 
    d. Using a loop starting at index 1, compare if both current index and prior index is_consonant()
    e. Increment counter by 1 if the above is true 
    f. Return the final counter number 
3. Create a sort_by_consonant_count() function 
    a. Declare an empty dictionary to store the results 
    b. Loop through each string in the list and store num_adj_consonants() as a value with string as key
    c. Sort the dictionary by values in descending order
    d. Return a list of the sorted keys
"""
def is_consonant(character):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return character.isalpha() and character not in vowels

def num_adj_consonants(string):
    num_adj_consonants = 0
    letters = string.replace(" ","")
    for i in range(len(letters) - 1):
        if is_consonant(letters[i]) and is_consonant(letters[i + 1]):
            num_adj_consonants += 1
    return num_adj_consonants

def sort_by_consonant_count(lst):
    sorted_lst = sorted(lst, key=num_adj_consonants, reverse=True)
    # print()
    # print(lst)
    # print([num_adj_consonants(x) for x in sorted_lst])
    return sorted(lst, key=num_adj_consonants, reverse=True)


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

"""
Note: 
sorted() maintains the original order of tied elements in the output. 
This behavior is known as stable sorting.
"""