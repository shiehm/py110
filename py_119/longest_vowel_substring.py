"""
Problem:
Given a string (non-empty, all lowercase alpha), return the length of the longest vowel substring. 

Rules:
- The vowels of interest are "a", "e", "i", "o", and "u".
- Argument will be non-empty string 
- The string consists entirely of lowercase alphabetic characters

I/O: Str/Int

Algorithm:
We will iterate through the characters, building a valid substring until we reach a non-valid char
Save this substring to a results list, then find the longest substring in the results list 

1. Initialize 
    a. vowels = 'aeiou'
    b. substring = ''
    c. results = []
2. Iterate through the string:
    a. if char in vowels substring += char 
    b. else append substring to results and reset the substring 
3. After the loop exits, append the remaining substring to the results list (it won't if the last letter is a vowel)
4. Find the max length by using max([len(string) for string in results]) and return it 
"""
def longest_vowel_substring(string):
    vowels = 'aeiou'
    substring = ''
    results = []
    for char in string:
        if char in vowels:
            substring += char
        elif substring:
            results.append(substring)
            substring = ''

    if substring:
        results.append(substring)
        
    counts = [len(x) for x in results]
    return 0 if not counts else max(counts)

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)