"""
Problem:
Take a string and return True is all enclosing characters: (), [], and {} are 
matched, with the opening coming first. Return False otherwise. 

Notes:
- We can use a score to track opener "debt" that gets paid off with a closer
- These scores must be specific to each kind of opener or closer 
    - We can use separate variables to store each kind:
        - parentheses
        - brackets
        - curly_braces
- Can break the checking if closer comes first, and is balanced into 2 functions

Algorithm:
- Create the opener/closer variables 
- Iterate through the string char by char 
- If the char is an opener, add +1 to its score variable
- If the char is a closer, -1 to its score variable
- If the variable is ever negative for any score, return False
- If any score is positive at the end, return False 
"""

MATCHES = {
    'parentheses' : ['(', ')'],
    'brackets' : ['[', ']'],
    'curly_braces' : ['{', '}']
}

def is_balanced(string):
    
    scores = {
        'parentheses' : 0,
        'brackets' : 0,
        'curly_braces' : 0
    }
    
    for pair in MATCHES:
        for char in string:
            if char == MATCHES[pair][0]:
                scores[pair] += 1
            elif char == MATCHES[pair][1]:
                scores[pair] -= 1
            
            if scores[pair] < 0:
                return False
    
    return sum(scores.values()) == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True