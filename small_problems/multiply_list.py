list1 = [3, 5, 7]
list2 = [9, 10, 11]

def multiply_list(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] * list2[i])
    return new_list

print(multiply_list(list1, list2) == [27, 50, 77])  # True

"""
I like this solution:

def multiply_list(numbers1, numbers2):
    return [a * b for a, b in zip(numbers1, numbers2)]
"""