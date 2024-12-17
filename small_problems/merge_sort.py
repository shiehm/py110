"""
Problem: 
- Take a list and keep splitting it into half lists until you have lists of 1 

Notes:
- Looks like I got the breakdown correct, I simply forgot that we alreay had
  a merge function that does what I needed from the last exercise
- It works with the function I made in the last exercise too
- The biggest difference is stating the return value as separate variables and 
  calling the merge function on the result to re-merge the list
"""

# def merge(list1, list2):
#     copy1 = list1[:]
#     copy2 = list2[:]
#     result = []
#     while copy1 and copy2:
#         if copy1[0] <= copy2[0]:
#             result.append(copy1.pop(0))
#         else:
#             result.append(copy2.pop(0))
#     return result + copy1 + copy2


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


def merge_sort(lst):
    mid = len(lst) // 2
    if len(lst) == 1:
        return lst
    
    sub_lst1 = merge_sort(lst[:mid])
    sub_lst2 = merge_sort(lst[mid:])
    
    return merge(sub_lst1, sub_lst2)


# All of these examples should print True
print(merge_sort([[1, 2], [2, 4], [3, 1]]))
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)