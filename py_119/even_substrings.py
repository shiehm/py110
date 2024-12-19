"""
Problem: 
Given a string of digits, find how many even-numbered substrings that can be formed. 

Examples:
- In the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

Rules:
- Numbers can only form sequentially (i.e. 2nd number has to come after the 1st) 
- If a substring occurs more than once, you should count each occurrence as a separate substring (the indicies are what matters) 
- Can be single digit

Algorithm: 
- Find all possible substrings of digits
    - Can use 2 for loops to iterate through indices
    - Return a lst of strings
- Find how many of these substrings are even
- Can be 2 separate functions 

substrings:
- Initialize a results = [] variable
- Start with a for loop for the starting index
    - Inner for loop starting with the outer loop + 1 through length of the string 
    - Append each substring to results
- Return the results 

even_substrings:
- Given the results list above
- Can use list comprehension [num for num in lst if int(num) % 2 == 0] 
"""

def substrings(string):
    results = []
    for start_idx in range(len(string)):
        for end_idx in range(start_idx + 1, len(string) + 1):
            substring = string[start_idx: end_idx]
            results.append(substring)
    return results

def even_substrings(string):
    lst = substrings(string)
    evens = [num for num in lst if int(num) % 2 == 0]
    return len(evens)

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)