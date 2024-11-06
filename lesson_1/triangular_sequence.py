"""
Problem:
- Input: Integer representing the row
- Output: Integer representing sum of the row
- Explicit Requirements:
    - Sequence of consecutive integers
    - Begins with 2, goes up by 2 so all even
    - Grouped in rows 
- Implicit
    - Each row has the same number of integers as the row number
- Example:
    - 2
    - 4, 6
    - 8, 10, 12
    - 14, 16, 18, 20
Examples / Test Cases:
- 1 = 2
- 2 = 10
- 3 = 30
- 4 = 68

Data Structures:
- Use slicing with a range to get the sequence of even integers to sum 
- Return the result as a single integer 

What we need:
- One cumulative sum that gives the amount of integers that have passed. Row numbers go up 1 and tells you how many digits there are
- Multiply the above by 2 to get the end => One range that gives the consecutive even digit incrementation: range(2, end, 2)

Algorithm:
- Create a function for that takes the row number and returns how many consecutive integers there are up through the row: 
    - Take the integer representing the row, and take the sum of that integer + (integer - 1) all the way to 0 using a recursive function 
- Create a function the finds the sum of the row:
    - Use a range to get the consecutive even integers, stepping by 2
    - The result - the row number gives you the start of the range to use in the slicing [start_index:]
    - Multiply the return value of the above function by 2, then + 1 to get the end of the range(2, end_value, 2)
    - Sum up the integers in the range(2, end_value, 2)[start_index: ] 

"""

def cumulative_integers(integer):
    if integer == 0:
        return 0
    else:
        return integer + cumulative_integers(integer - 1) 

def triangular_sum(integer):
    start_index = cumulative_integers(integer) - integer
    end_value = cumulative_integers(integer) * 2 + 1
    return sum(range(2, end_value, 2)[start_index:])

for i in range(1, 5):
    print(f'Row {i} has a sum of {triangular_sum(i)}')