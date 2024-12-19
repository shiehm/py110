"""
Problem:
Given two strings, return True if some portion of the characters in the first string can be rearranged to match the characters in the second. 

Rules: 
- Both string arguments only contain lowercase alphabetic characters. 
- Neither string will be empty.
- Not all the letters in the first need to be used 
- Assuming that frequency matters (i.e. if there are 2 'a's in the first, can only use 2 'a's in the 2nd)

Data Structure: May use list as intermediary to be easier to work with 

Algorithm:
- Can do this iteratively by going through each letter of the 2nd. 
- If the letter in the first is in the second (if char in second):
    - second -= char
    - Else: return False
- Return True at the end 
"""

def unscramble(scramble, word):
    remainder = list(scramble)
    for letter in word:
        if letter in remainder: 
            remainder.remove(letter)
        else:
            return False
    return True 

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)