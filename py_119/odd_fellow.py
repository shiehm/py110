"""
Problem:
- Given a list of integers, return the integer that appears an odd number of times. 

Rules:
- There will always be exactly one such integer in the input list.

Strategy:
- Get a count of how many times each one appears, then return the number that appears if count % 2 != 0
- Can use a dictionary to store results of counts 

Algorithm:
- Use a dictionary comprehension to get the counts for each integer 
    - counts = {num: lst.count(num) for num in lst}
- Use a list comprehension to get the key where the value % 2 != 0
    - odds = [num for num in counts if counts[num] % 2 != 0]
- Return the only value in this list 
    - return odds[0]
"""

def odd_fellow(lst):
    counts = {num: lst.count(num) for num in lst}
    odds = [num for num in counts if counts[num] % 2 != 0]
    return odds[0]

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)