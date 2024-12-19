"""
Problem: Given a list of int find the number of identical pairs 

Examples:
For instance, the number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

Rules:
- If the list is empty or contains exactly one value, return 0.
- If a certain number occurs more than twice, count each complete pair once. 
    - For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2. 

I/O: List / Int

Algorithm:
We can do something similar to the dictionary count frequencies:
- Count the occurances of each number in the list with a dic comprehension
- For each value in the dictionary do floor division by 2 
- Sum up these values and return the result (sum of empty dictionary / list is 0 so we're OK) 
"""

def pairs(lst):
    count_dic = {num: lst.count(num) // 2 for num in lst}
    return sum(count_dic.values())
    
    # if not lst:
    #     return 0
    # else:
    #     return list(count_dic.values())[0]

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]))
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]))
print(pairs([]))
print(pairs([23]))
print(pairs([997, 997]))
print(pairs([32, 32, 32]))
print(pairs([7, 7, 7, 7, 7, 7, 7]))

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)