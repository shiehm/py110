"""
Write a function that takes a list of integers between 0 and 19 and returns 
a list of those integers sorted based on the English word for each number:

Algorithm:
1. Create a dictionary matching strings to integers for numbers 0 - 19 --> done in global scope
2. Match each number in the input list with its alpha name --> Done in helper function 
3. Sort by the alpha name 
4. Strip out the integer list sorted, and return it 
"""

string_nums = 'zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen'
lst_nums = string_nums.split(', ')
dict_nums = {key: value for key, value in zip(list(range(0,20)), lst_nums)}

# Note: You don't need dict_nums since the nums are already ordered 0-19. 

def alphabetic_number(num):
    return dict_nums[num]

def alphabetic_number_sort(lst):
    return sorted(lst, key=alphabetic_number)

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True