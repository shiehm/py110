def rotate_rightmost_digits(digits, place):
    lst_digits = list(str(digits))
    digit_selected = lst_digits.pop(-place)
    new_lst = lst_digits + [digit_selected]
    return int(''.join(new_lst))

def max_rotation(digits):
    for i in range(len(str(digits)), 0, -1):
        digits = rotate_rightmost_digits(digits, i)
    print(digits)
    return digits

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True