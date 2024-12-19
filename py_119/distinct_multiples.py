"""
Problem: 
Find the number of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. 
- Input: String
- Output: Integer

Rules:
- You may assume that the input string contains only alphanumeric characters.

Data Structure:
- Can use a dictionary comprehension to store the letter and the counts
- Dictionaries are good for this because they'll only store the letter once with the last iteration 

Algorithm:
- First make the string lower
- Create a dictionary with the letters as keys and the counts as frequencies
    - letter: string.count(letter) for letter in string
- Using a list / comprehension, find the letters than have counts > 1 
- Return the length of this list
"""

def distinct_multiples(string):
    lower = string.lower()
    counts = {char: lower.count(char) for char in lower}
    frequent = [char for char in counts if counts[char] > 1]
    return len(frequent)

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5