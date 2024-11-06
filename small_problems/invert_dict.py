"""
Problem: Build a function that takes a dictionary and returns a dictionary with 
the original keys and values swapped.

Questions:
- Return the same dictionary? Or a new one? Or doesn't matteR?

Input: Dictionary
Output: Dictionary

Algorithm:
- Unpack dictionary with items()
- Use dictionary comprehension to create new dictionary
"""

def invert_dict(dic):
    return {value: key for key, value in dic.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True