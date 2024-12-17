# Solved it first brute force method

lst = [14, 15, 16, 17, 18, 19, 20, 21]

for i in range(len(lst)):
    if lst[i] < 20:
        lst[i] -= 9
    else:
        lst[i] -= 18
        
print(lst)  # [5, 6, 7, 8, 9, 10, 2, 3]


# Solve it like a cup

lst = [14, 15, 16, 17, 18, 19, 20, 21]

for i in range(len(lst)):
    str_nums = str(lst[i])
    lst_nums = list(str_nums)
    int_nums = [int(num) for num in lst_nums]
    lst[i] = sum(int_nums)

print(lst)  # [5, 6, 7, 8, 9, 10, 2, 3]


# Solve it with Modolo

lst = [14, 15, 16, 17, 18, 19, 20, 21]

for i in range(len(lst)):
    if lst[i] % 9 == 0:
        lst[i] = lst[i] // 2
    elif lst[i] % 9 == 1:
        lst[i] = lst[i] - 9
    else:
        lst[i] = lst[i] % 9

print(lst)