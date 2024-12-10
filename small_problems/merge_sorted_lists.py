"""
Problem: Create a function that takes 2 sorted lists and creates a merged list 
in ascending order, without using sort or sorted. You must build the result list 
one element at a time in the proper order.

Requirements:
- Lists will all contain the same type (i.e. all int or all str)

Input: 2 lists
Output: One new list (don't mutate the existing lists)

Notes:
- We could use bubble sort here on a combined list... 
- But it says one element at a time, so I assume that means taking each next 
  element and comparing it then appending the lowest one first. 
- It's possible that the 1st of the next pair will be lower than the 2nd of the 
  preceeding pair, so it seems like we need some sort of "find next lowest" 

Algorithm:
- Create an empty list to hold the result
- Create a new combined list with the 2 lists
- Create a variable to hold the lowest value
- Use min() to find the lower value then index() to find the index with which to 
  pop() and save it to that lowest value variable 
- Append the lowest value variable to the result list
- Repeat this process until the merged list is empty
"""

def merge(lst1, lst2):
    result_lst = []
    merged_lst = lst1 + lst2
    lowest_value = ''
    for _ in range(len(merged_lst)):
        lowest_value = min(merged_lst)
        result_lst.append(lowest_value)
        lowest_index = merged_lst.index(lowest_value)
        merged_lst.pop(lowest_index)
    return result_lst

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)

"""
The LS solution is interesting, just using an if/else to solve the problem of
how to append in the proper order. Popping the appended elements means the list
comparison starts back over, so you never need to compare beyond the two idx 0s.

def merge(list1, list2):
    copy1 = list1[:]
    copy2 = list2[:]
    result = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            result.append(copy1.pop(0))
        else:
            result.append(copy2.pop(0))

    return result + copy1 + copy2
"""