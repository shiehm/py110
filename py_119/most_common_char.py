"""
Problem: For a given string, return the character that occurs most often.

Requirements:
- Return the first character if there are ties
- Assume both upper and lowercase to be the same 
- Do spaces count as a character? Exclamation and grammer? 

Data Structure:
I/O: String / String 1 character
- Might use list as intermediate structure to work with data
- Might use dictionary to store results of count for each letter 

Algorithm:
We can do this 2 ways:
- Iteratively keeping track of the most frequent character so far
- Finding all character's counts and then the greatest of the characters

Other Thoughts:
- We can use the string count method 
- We can use dictionary comprehension to quickly generate a dictionary with counts
- What does a dictionary do with multiple of the same keys? 
    - It only stores it once (each additional time overrides it so it stores the last one which is going to be the same)
- Will write out algorithm for an iterative loop for all characters first before trying a comprehension 

1. Turn the string into all lower
2. Loop:
    a. Create an empty dictionary to house the results 
    b. Iterating through each character in the string, assign dic[char] = string.count(char)
    c. Can use a condition, if dic.get(char) != None before proceeding to make sure we only get one 
3. Find the maximum counts, can do something like max(list(dic.values()))
    a. result = [char for char in dic if dic[char] == max]
    b. result[0]
4. Return result
"""

def most_common_char(string):
    lower_string = string.lower()
    count_dic = {char: lower_string.count(char) for char in lower_string if char.isalpha()}
    max_value = max(count_dic.values())
    most_common = [char for char in count_dic if count_dic[char] == max_value]
    return most_common[0]

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')