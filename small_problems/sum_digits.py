def sum_digits(num):
    total = 0
    for num in str(num):
        total += int(num)
    return total

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

def sum_digits(num):
    lst_nums = [int(num) for num in str(num)]
    return sum(lst_nums)

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True