# Find the longest substring in alphabetical order.
# Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
# The input will only consist of lowercase characters and will be at least one letter long.
# If there are multiple solutions, return the one that appears first.

"""
Problem: Find the longest consecutive substring in alphabetical order 
Examples: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
Requirements:
- The input will only consist of lowercase characters and will be at least one letter long.
- If there are multiple solutions, return the one that appears first.

Input: String, only lowercase alphabetical letters with no spaces
Output: String sub-string

Rules for substring:
- The following letter must be > than the prceeding 

Data Structure: Think of the intermediate steps 
- Hard to iterate over a string, so may be easier to turn it into a list
- Think about variable names 

Algorithm:
- Come up with a 1-3 sentence strategy first 
- Idea is to come up with an idiot proof algorithm FIRST before coding 

High Level:
1. Find all substrings that adhere to rules
    a. Iteratively add each valid characters to a sub-string placeholder until you reach an invalid letter
    b. Add this substring to a results list
    c. Restart with the next sub-string
    d. When the loop finishes, add the last sub-string
2. Find the longest substring in this collection

Detailed Implementation:
1. Create a 
    a. result variable to hold sub-strings, and 
    b. a variable to hold the last character initialized with '', and 
    c. one to hold the sub-string
2. Iterate through the characters in the string, and 
    a. If it is greater than, add it to the sub-string
    b. If you reach an invalid character, append the sub-string to the result list 
    c. Restart the last character and sub-string variables with the current character
    d. Append the last sub-string to the list (might get appended twice but that's OK) 

    New Function:
    
3. Once you've reached the end of the string, find the longest sub-string in the list and return it 
    a. Can't just find max becaues there may be multiple, so iteratively go through the sub-string list
    b. If the length of the substring is greater than the max (set at 0 initially), save it and its length
    c. Return the longest sub-string saved to a variable

Note: It's OK to do the brute force method first before changing. It's like writing a draft. 
- Create all possible substrings
- Filter for those that are in alphabetical order
- Find the longest substrings
- Return the first longest substring

This is a common parttern: 
- Find all possible solutions 
- Find the ones that fit rules 
- Find the best one out of those 

Can restart and start from scratch 
Can just say I'm stuck and pause and think 
"""

def find_subs(string):
    results = []
    sub_string = ''
    last_char = ''    
    for char in string:
        if char >= last_char:
            sub_string += char
            last_char = char
        else:
            results.append(sub_string)
            sub_string = char
            last_char = char
    results.append(sub_string)
    return results

def longest(string):
    subs = find_subs(string)
    max_len = 0
    longest = ''
    for sub in subs:
        if len(sub) > max_len:
            longest = sub
            max_len = len(sub)
    return longest

# Tests
print(find_subs('asd'))
print(find_subs('nab'))
print(find_subs('abcdeapbcdef'))
print(find_subs('asdfaaaabbbbcttavvfffffdf'))
print(find_subs('asdfbyfgiklag'))
print(find_subs('z'))
print(find_subs('zyba'))

print(longest('asd') == 'as')
print(longest('nab') == 'ab')
print(longest('abcdeapbcdef') ==  'abcde')
print(longest('asdfaaaabbbbcttavvfffffdf') == 'aaaabbbbctt')
print(longest('asdfbyfgiklag') == 'fgikl')
print(longest('z') == 'z')
print(longest('zyba') == 'z')