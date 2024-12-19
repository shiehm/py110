"""
Problem: 
Given a string determins if it is a pangram (True/False).

Input: String
Output: Boolean

Details:
- Pangrams are sentences that contain every letter of the alphabet at least once. 
- For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram 
  since it uses every letter at least once. Note that case is irrelevant.

Rules:
- Every letter has to be used at least once (multiple times don't matter)
- Case doesn't matter 
- Spaces, special characters, other things don't matter 
- Assuming every input is a sentence, assuming grammer and spelling don't matter for this 

Algorithm:
- Turn the string into all lower() to make it case insensitive 
- Initialize a variable with all the letters 26 of them 
- We can iterate through all the letters of the alphabet and return false once we find one that doesn't appear
- Return true at the end
"""

def is_pangram(string):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alpha:
        if letter not in string.lower():
            return False
    return True

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)