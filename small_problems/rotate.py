"""
Write a function that rotates a list by moving the first element to the end 
of the list. Do not modify the original list; return a new list instead.

If the input is an empty list, return an empty list.
If the input is not a list, return None.
"""

def rotate_list(lst):
    if not (type(lst) == list):
        return None
    elif not lst:
        return []
    else:
        return lst[1:] + [lst[0]]

# Launch School solution:
def rotate_list_answer(lst):
    if not isinstance(lst, list):
        return None

    if len(lst) == 0:
        return []

    return lst[1:] + [lst[0]]

# # All of these examples should print True
# print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
# print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
# print(rotate_list(['a']) == ['a'])
# print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
# print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
# print(rotate_list([]) == [])

# # return `None` if the argument is not a list
# print(rotate_list(None) == None)
# print(rotate_list(1) == None)

# # the input list is not mutated
# lst = [1, 2, 3, 4]
# print(rotate_list(lst) == [2, 3, 4, 1])
# print(lst == [1, 2, 3, 4])

"""
Write a function that rotates the last count digits of a number. 
To perform the rotation, move the first of the digits that you want to 
rotate to the end and shift the remaining digits to the left.
"""

def rotate_rightmost_digits(digits, place):
    lst_digits = list(str(digits))
    digit_selected = lst_digits.pop(-place)
    new_lst = lst_digits + [digit_selected]
    return int(''.join(new_lst))

# print(rotate_rightmost_digits(735291, 2) == 735219)  # True
# print(rotate_rightmost_digits(735291, 3) == 735912)  # True
# print(rotate_rightmost_digits(735291, 1) == 735291)  # True
# print(rotate_rightmost_digits(735291, 4) == 732915)  # True
# print(rotate_rightmost_digits(735291, 5) == 752913)  # True
# print(rotate_rightmost_digits(735291, 6) == 352917)  # True
# print(rotate_rightmost_digits(1200, 3) == 1002)      # True

"""
Problem:
Take the number 735291 and rotate it by one digit to the left, getting 352917. 
Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. 
Keep the first two digits fixed in place and rotate again to get 321759. 
Keep the first three digits fixed in place and rotate again to get 321597. 
Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. 
The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the 
maximum rotation of that integer. You can (and probably should) 
use the rotate_rightmost_digits function from the previous exercise.

1. Move the 1st place digit to the last place
2. Keep the 1st digit and move the 2nd to last place.
3. Keep the 1st 2 digits and move the 3rd to last.
4. Keep the 1st 3 digits and move the 4th to last.
and on and on until you're out of digits to rotate 
"""

def max_rotation(digits):
    for i in range(len(str(digits)), 0, -1):
        digits = rotate_rightmost_digits(digits, i)
    return digits

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True