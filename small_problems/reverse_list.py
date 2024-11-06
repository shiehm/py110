"""
Problem:
Write a function that takes a list as an argument and reverses its elements, 
in place. That is, mutate the list passed into the function. The returned 
object should be the same object used as the argument.

Requirements:
- You may not use the list.reverse method 
- nor may you use a slice ([::-1]).
- Must be in-place (mutating object)

Input: List
Output: Same list 

Notes:
- When you reassign an element, it mutates the list keeping the list the same 
- We can use element reassignment to maintain the same list 
- We can use negative indexing to iterate through 

Algorithm:
1. Measure the length of the list 
2. Create a copy of the list to use as a reference for reassignment 
3. Loop through the elements of the list and assign each element equal to its 
   index going backwards on the copied list (i.e. index 0 = copied index -1)
"""

def reverse_list(lst):
    lst_copy = list(lst)
    for i in range(len(lst)):
        lst[i] = lst_copy[-(i + 1)]
    return lst

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4)
print(result4 == [])                        # True
print(list4 is result4)                     # True