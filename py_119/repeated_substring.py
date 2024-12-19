"""
Problem:
Given a string consisting of repeating strings, find the repeating component and how many times it repeats

Details: 
Given a nonempty string return a tuple consisting of a string and an integer:
If we call the string argument s, the string component of the returned tuple t, and the integer component of the tuple k, then 
s, t, and k must be related to each other such that s == t * k. 
The values of t and k should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

Rules:
- You may assume that the string argument consists entirely of lowercase alphabetic letters.
- Single characters can work too if it is the shortest substring that repeats 
- Does the repeating sub-string always start at index 0? Examples seem like it does 
- Does the string have to consist entirely of the substring (i.e. no other characters or patterns?). Examples seem like it does 

Algorithm: 
We can split this problem into 2 parts:
- Finding the shortest possible substring that repeats (with the largest repeat count)
- Finding how many times it repeats 

Ideas:
- Can use string count method 
- Can use the in operator 
- Can iteratively test for each substring tested:
    - How many times does it appear in the string (count)
    - Does that match up with len(string) / len(substring) 
    - If it does, then save it to a dictionary substring: count 

Algorithm:
1. Initialize an empty dictionary to hold results 
2. Using a for loop with end_inx starting at index 1 and going to len(string):
    a. Count how many times substring = string[0: end] appears
    b. Count len(string) / len(string[0: end])
    c. if a == b then dictionary[substring] = count 

This could be a separate function:
3. Find the max value and save it to a variable 
4. For substring in dictionary, if dictionary[substring] == max value, store it to results (there will only be unique ones if rules valid)
5. Return (substring, dictionary[substring])
"""

def find_substring(string):
    results = dict()
    for end_idx in range(1, len(string) + 1):
        substring = string[0: end_idx] # Remember when using the generated index that range will not incl. the end, so need to + 1
        count = string.count(substring)
        places = len(string) / len(substring)
        if count == places:
            results[substring] = count
    return results

def repeated_substring(string):
    results = find_substring(string)
    highest = max(results.values())
    matches = [key for key, value in results.items() if value == highest]
    return (matches[0], highest)

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))