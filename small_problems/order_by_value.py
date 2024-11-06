"""
Given a dictionary, return its keys sorted by the values associated with each key.

Input: Dictionary
Output: List

Algorithm: 
1. Create a helper function that returns the key for a value 
2. Sort the dictionary using the helper funciton 
3. Return a list of the keys 
"""

def order_by_value(my_dict):
    keys_sorted = sorted(my_dict.items(), key=lambda x: x[1])
    # list_sorted = list(zip(*keys_sorted))
    # return list(list_sorted[0])
    return [key for key, value in keys_sorted]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']

print(order_by_value(my_dict))
print(order_by_value(my_dict) == keys)  # True