"""
Given a sequence of integers, filter out instances where the same value occurs 
successively, retaining only the initial occurrence. Return the refined sequence.
"""

def unique_sequence(lst):
    last_num = lst[0]
    new_lst = [last_num]
    for num in lst:
        if num != last_num:
            new_lst.append(num)
        last_num = num
    return new_lst

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
print(unique_sequence(original))


"""
This is a super elegant solution, dictioanries don't allow dupe keys!
"""

def unique_sequence(nums):
    return list(dict.fromkeys(nums))