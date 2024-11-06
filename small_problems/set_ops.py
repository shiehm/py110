"""
Given two lists, convert them to sets and return a new set which is the union of both sets.
"""

# def merge_sets(list1, list2):
#     set1 = set(list1) 
#     set2 = set(list2)
#     return set1.union(set2)

def merge_sets(list1, list2):
    return set(list1) | set(list2)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True

"""
Transform two lists into frozen sets and find their common elements.
"""

def intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True

"""
From two list arguments, determine the elements that are unique to the first list. 
The return value should be a set.
"""

# def unique_from_first(list1, list2):
#     unique = set()
#     for num in list1:
#         if num not in list2:
#             unique.add(num)
#     return unique

def unique_from_first(list1, list2):
    return set(list1) - set(list2)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]

print(unique_from_first(list1, list2))
print(unique_from_first(list1, list2) == {9, 3})