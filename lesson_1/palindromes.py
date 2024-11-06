"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection should be case-sensitive.

Test Cases:

Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]

Input: String
Output: List of sub-strings
Requirements:
    Explicit:
    - Substrings must be 2 or more characters
    - Palindromes are case-sensitive
    
    Implicit:
    - Empty strings return empty strings
    - Sub-string palindromes can be part of larger sub-string palindromes

Data Structures: List 
Algorithm (2-parts)
    Sub-string Algorithm: Create a function that returns every substring 2 characters or longer in a string
    1. Declare a result variable and set it to an empty list 
    2. Create an outer loop starting from index 0 to the length of the string - 1 (to account for 2-char), for the starting position of the sub-string
    3. Create an inner loop starting from the starting index + 2 (b/c end is exclusive in slicing and range) to the length of the string + 1, for the ending position of the sub-string
    4. Append each result to the list
    5. Return the list

    Palindrome Algorithm:
    1. Declare a result variable and set it to an empty list 
    3. Pass in the string argument to the sub-string function
    2. Use a loop to iterate through each sub-string in the list, and test whether each sub-strings = itself reversed 
    3. If it does, save it to the result list
    4. Return the result list
"""

def substring(string):
    substrings = []
    for i in range(len(string) - 1): # This is the starting index, so it'll go from 0 to the 2nd to last, since range is exclusive of the ending 
        for e in range(i + 2, len(string) + 1): # Note this needs the + 1 otherwise it'll be ending with e = range(7, 7) which returns nothing 
            substrings.append(string[i:e])
    return substrings

def palindrome(string):
    palindromes = []
    lst = substring(string)
    for word in lst:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes

print(palindrome("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
print(palindrome("palindrome")) # []
print(palindrome(""))           # []
print(palindrome("repaper"))    # ['repaper', 'epape', 'pap']
print(palindrome("supercalifragilisticexpialidocious")) # ["ili"]