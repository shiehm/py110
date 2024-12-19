"""
Problem: 
- Given a list of numbers, all of which are the same except one. 
- Find and return the number in the list that differs from all the rest.

Rules:
- The list will always contain at least 3 numbers, and there will always be exactly one number that is different.

Algorithm:
- Create a dictionary comprehension to get the counts 
- Return the one where the value == 1
"""

def what_is_different(lst):
    counts = {num: lst.count(num) for num in lst}
    unique = [num for num in counts if counts[num] == 1]
    return unique[0]

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)