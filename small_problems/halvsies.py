# If it is an odd length, max index will be even. (5 elements, 4 max index = 2 half point, can +1 to use for split)
# If it is even number of elements, max index will be odd (10 elements, 9 max index = 5 floor div half, use for split)


def halvsies(lst):
    length = len(lst)
    if length % 2 != 1:
        mid = int(length / 2)
    else:
        mid = int(length // 2 + 1)
        
    return [lst[:mid], lst[mid:]]

"""
Actually, since floor division removes the decimals, you can just + 1 before // 2
for both even and odd, since odds will correct and then evens will drop the .5

def halvsies(lst):
    half = (len(lst) + 1) // 2
    first_half = lst[:half]
    second_half = lst[half:]
    return [first_half, second_half]
"""

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

print(halvsies([1, 2, 3, 4]))
print(halvsies([1, 5, 2, 4, 3]))
print(halvsies([5]))
print(halvsies([]))