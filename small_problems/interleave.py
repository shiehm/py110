def interleave(lst1, lst2):
    zip_list = zip(list1, list2)
    new_list = []
    for i in zip_list:
        new_list.append(i[0])
        new_list.append(i[1])
    return new_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]

print(interleave(list1, list2))
print(interleave(list1, list2) == expected)      # True