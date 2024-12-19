"""
Problem:
Given two strings, find the number of times that the second occurs in the first. 

Rules
- 2nd string is never empty, but first string could be empty
- Overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

Input: String
Output: Integer

High-level strategy:
- First we can have a guard clause, if the 2nd string is len > 1st, return 0 
- The difficulty will be the fact that overlapping strings don't count
- The best way is to do it iteratively, 
    - Go from index 0 to length of the 2nd string,
    - if it is a match, save it (count+=1) and start the search from the index +1 after the end length
    - if not, start search from index +1 after beginning length 
- Can use a while loop, while beginning index is <= length - len(second) 

Algorithm:
1. Inset guard clause
2. Initialize variables: 
    a. count = 0, 
    b. start = 0
    c. end = len(second)
3. While start is less than or equal to len(first) - len(second):
    a. if first[start, end] == second, increase count += 1, set start to end + 1, end to start + length of 2nd
    b. else start + 1, end + 1
4. Return count

"""

def count_substrings(first, second):
    if len(second) > len(first):
        return 0
    
    count = 0
    start = 0
    end = len(second)
    
    while end <= len(first):
        if first[start: end] == second:
            count += 1
            start = end
            end = start + len(second) 
        else:
            start += 1
            end += 1
    return count

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)