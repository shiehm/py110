def layers(nested_lst):
    if not isinstance(nested_lst, list):
        return 0
    return 1 + max([layers(lst) for lst in nested_lst])

def flatten(nested_lst):
    flat = []
    for item in nested_lst:
        if isinstance(item, list):
            flat.extend(flatten(item)) # wrapping a flatten(item) will cause it to check the inner, and either return a list or the innermost elements to append via else if it isn't a list
        else:
            flat.append(item)
    return flat

# Before my edits, I had a standalone flatten and then a different multi-flatten

# def flatten(nested_lst):
#     flat = []
#     for item in nested_lst:
#         if isinstance(item, list):
#             flat.extend(item) # wrapping a flatten(item) will cause it to check the inner, and if it isn't a list just append
#         else:
#             flat.append(item)
#     return flat

# def multi_flatten(nested_lst):
#     depth = layers(nested_lst)
#     flat = nested_lst
#     for _ in range(depth - 1):
#         flat = flatten(flat)
#     return flat
    
nested = [1, [2, 3, [4, 5]], [6, [7, 8]]]
print(flatten(nested))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

nested2 = [1, 2, 3, [4, 5], [6, 7, 8]]
print(flatten(nested2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]