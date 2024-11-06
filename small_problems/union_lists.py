# def union(lst1, lst2):
#     combo_lst = lst1 + lst2
#     union_set = set()
#     for element in combo_lst:
#         union_set.add(element)
#     return union_set

def union(lst1, lst2):
    union_set = set(lst1 + lst2)
    return union_set

print(union([1, 3, 5], [3, 6, 9])) 
print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True