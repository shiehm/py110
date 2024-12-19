"""
Problem:  For a list of numbers, return a list counting how many numbers in the list are smaller than each number. 

Requiremetns:
- Only count unique values
- Return a value for each number in the list (each element will be an input) 

Input: List of numbers
Output: List of frequencies

Algorithm: 
We want to take each number and count how many unique numbers in the list are smaller than it.
We can break the problem down:
- Get all unique numbers in the list. We can use set() for this 
- Count the frequency that the expression num < comparison_num is True
We can separate out the solution into functions:
- Generate the unique numbers in the set
- Given a number and the set of comparisons, a function that tells how many unique numbers are smaller than it 

1. Initialize 
    a. unique_nums and assign it to set(lst)
    b. smaller_than and assign it to []
2. Use a for loop to iterate through the num in lst:
    a. Use a list comprehension --> [x for x in unique_nums if x < num]
    b. Use len to count this list 
    c. Append this number to smaller_than
3. Return smaller_than
"""

def smaller_numbers_than_current(lst):
    unique_nums = set(lst)
    smaller_than = []
    for num in lst:
        count = len([x for x in unique_nums if x < num])
        smaller_than.append(count)
    return smaller_than

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)