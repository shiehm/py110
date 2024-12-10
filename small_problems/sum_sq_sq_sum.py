def sum_square_difference(num):
    nums = list(range(1, num + 1))
    squares = [n**2 for n in nums]
    sq_sum = sum(nums)**2
    sum_sq = sum(squares)
    return sq_sum - sum_sq

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True