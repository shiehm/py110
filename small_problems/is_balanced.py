"""
Problem: 
Write a function that takes a string as an argument and returns True if all 
parentheses in the string are properly balanced, False otherwise. To be 
properly balanced, parentheses must occur in matching '(' and ')' pairs.

Requirements:
- An opening parenthesis must come before, and be matched with a closing 

Notes:
- We can break down the positioning of the open and closed parenthesis with idx
- Every open ( needs a ) to follow it, regardless of how many chars or ( in btwn

Algorithm:
- Iterate through the characters in the string
- Check if a close comes first, if it does return false
- If the character is a (, search the rest of the string for )
- At the same time iterate through the string backwars
- If the char is ) search for (
- This way it checks that it is balanced

LS Answer:

def is_balanced(s):
    parens = 0
    for char in s:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        if parens < 0:
            return False
    return parens == 0

What would the written algorithm look like for the above?
- Iterate through the string char by char 
- Track open and close parentheses with this logic:
    - Create a "tick" for each open (
    - Close the "tick" for each close )
    - If a close comes before an open, return False (i.e. if a close comes before open)
    - If there are "ticks" left at the end of the loop, return False 
"""

def is_balanced(string):
    
    open_matches = []
    close_matches = []
    reverse_string = string[::-1]

    for i in range(len(string)):
        if string[i] == '(':
            match = string.find(')', i + 1)
            open_matches.append(match)
        if reverse_string[i] == ')':
            match = reverse_string.find('(', i + 1)
            close_matches.append(match)
    
    return -1 not in open_matches and -1 not in close_matches

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True