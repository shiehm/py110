"""
Problem: From a list of integers, return a pair (as a tuple) that is the closest together

Requirements:
- If multiple pairs are tied, return the first occurance

Questions:
- How do you measure which pair occurs first? By the first number I assume? 
- Assuming order of the pairs doesn't matter (i.e. (19, 25) = (25, 19) 
- Assuming we are measuring absolute distance (implications for using min if a difference is negative) 
- Assuming all inputs in lst will be integers

Data Structure:
- Store possible results as list of tuples 

Input: List
Output: Tuple

Algorithm:
- First we want to find all possible pairs of numbers as tuples
- Then we want to find the one with the smallest distance between them 
    - If there are multiple, keep the first result 
- Can split this into 2 functions:
    - One to generate all possible pairs 
    - One to find the pair with the smallest distance

Generate all pairs:
1. Given a list, 
    a. Initialize a results list
2. Use a nested for loop (for first in range(len(lst), for second in range(first + 1, range(len(lst)))
    a. Iterate through and generate pairs:
    b. results.append((first, second))
3. Return results list

Determine smallest distrance:
1. Given a list,
    a. Generate pairs = possible_pairs(lst)
    b. Initialize a "smallest_distance" variable and assign it to max(lst) - min(lst)
    c. Initialize a "smallest_pair" variable and assign it to None
2. Iterate through the pairs list:
    a. if abs(pairs[0] - pairs[1]) < smallest_distance
    b. Assign the difference to smallest_distance
    c. Assign the tuple to smallest_pair
3. Return smallest_pair

"""

def possible_pairs(lst):
    results = []
    length = len(lst)
    for first in range(length - 1):
        for second in range(first + 1, length):
            results.append((lst[first], lst[second]))
    return results

def closest_numbers(lst):
    pairs = possible_pairs(lst)
    smallest_distance = max(lst) - min(lst)
    smallest_pair = None
    for pair in pairs:
        distance = abs(pair[0] - pair[1])
        if distance < smallest_distance:
            smallest_distance = distance
            smallest_pair = pair
    return smallest_pair

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))