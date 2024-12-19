"""
Problem: Given a list of integers, find the minimum sum of 5 consecutive integers (return None if list is < 5)

Input: list of integers
Output: one integer, min sum of 5 consecutive integers

Requirements:
- If less than 5 in list return None
- Assuming list will always contain integers

Algorithm:
1. If list is less than 5 integers, return None
2. Find all possible sums of 5 consecutive integers. Can be a separate function
    a. Iterate through each index from 0 to len(lst) - 5
    b. Grab the sum of the 5 consecutive integers using slicing (i.e. num[i: i + 5]
    c. Store this result in a list 
3. Then find the minimum of these sums. 
"""

def consecutive_sums(lst):
    consecutive_sums = []
    for i in range(len(lst) - 4):
        total = sum(lst[i:i+5])
        consecutive_sums.append(total)
    return consecutive_sums

def minimum_sum(lst):
    if len(lst) < 5:
        return None
    
    return min(consecutive_sums(lst))

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)