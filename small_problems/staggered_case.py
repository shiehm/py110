"""
Write a function that takes a string as an argument and returns that 
string with a staggered capitalization scheme. Every other character, 
starting from the first, should be capitalized and should be followed 
by a lowercase or non-alphabetic character. Non-alphabetic characters 
should not be changed, but should be counted as characters for 
determining when to switch between upper and lower case.

Requirements:
- Looks like spaces are treated as a non-alpha char

Notes:
- Neither str.upper nor str.lower has any effect on non-alphabetic characters

Algorithm:
1. Create a new string to hold the result
2. Iterate through the characters via index numbers
3. For every even index incl. 0:
    3a. Check if it is alpha()
    3b. If it is, uppercase it 
    4c. If it is not, leave it
4. For every odd index:
    4a. Check if it is alpha()
    4b. If it is lowercase it
    4c. If it is not, leave it
5. Return the new string
"""

# def staggered_case(string):
#     new_string = ''
#     for i in range(len(string)):
#         if i % 2 == 0 and string[i].isalpha():
#             new_string += string[i].upper()
#         elif i % 2 != 0 and string[i].isalpha():
#             new_string += string[i].lower()
#         else:
#             new_string += string[i]
#     return new_string

def staggered_case(string):
    new_string = ''
    for idx, char in enumerate(string):
        new_string += char.upper() if idx % 2 == 0 else char.lower()
    return new_string

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True


"""
For extended study: 
Modify the function from the previous exercise so it ignores non-alphabetic 
characters when determining whether it should uppercase or lowercase each 
letter. The non-alphabetic characters should still be included in the return 
value; they just don't count when toggling the desired case.

Can use * -1 as a toggle
"""

def staggered_case(string):
    new_string = ''
    toggle = -1
    for char in string:
        toggle *= -1 if char.isalpha() else 1
        new_string += char.upper() if toggle == 1 else char.lower()
        
    return new_string
    
string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True