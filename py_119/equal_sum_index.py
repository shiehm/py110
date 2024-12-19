"""
Problem:
Given a list of integers return the index N for which 
- all numbers with an index less than N 
- sum to the same value as the numbers with an index greater than N. 

Rules:
- If there is no index that would make this happen, return -1.
- If you are given a list with multiple answers, return the index with the smallest value. (Return the first answer)
- The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the numbers to the right of the last element is 0.
- Based on examples, the pivot index is not included in either sum 

Strategy:
- Iterate through the indices starting with 0 (handles cases where all following nums are 0)
- Use a divisor and use slicing lst[:divisor] lst[divisor+1:]
- Summing[0:0] == 0 so that works 
- Use a for loop, for divisor in range(len(lst))
- Return -1 at the end 

Algorithm:
1. Use a for loop to iterate through mid through len(lst)
    a. Set left = lst[:mid]
    b. Set right = lst[mid+1:] --> This might throw an error on the last one, 
        - if divisor+1 == len(lst) --> right = 0
    c. If sum of left == right: return mid
2. Return -1 if no divisors are found 
"""

def equal_sum_index(lst):
    for mid in range(len(lst)):
        left = sum(lst[:mid])
        right = 0 if mid == len(lst) else sum(lst[mid+1:])
        if left == right:
            return mid
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)