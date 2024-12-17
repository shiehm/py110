"""
Alorithm:
- Find the middle value index using // 2
- If it matches the search value, return the index
- If it is greater than the search value, recursively call the lower half. 
- If it is lesser, recursively call the greater half 
"""

# The issue with this solution is that the in and not in keywords search through 
# the entire collection linerarly which defeats the purpose of binary search. 

def binary_search(collection, target):
    mid = len(collection) // 2
    if collection[mid] == target:
        return mid
    elif len(collection) == 1:
        return -1
    elif collection[mid] > target:
        return binary_search(collection[:mid], target)
    else:
        result = binary_search(collection[mid + 1:], target)
        return -1 if result == -1 else mid + 1 + result

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store', 'Donuts R Us', 'Eat a Lot', 'Good Food', 'Pasta Place', 'Pizzeria', 'Tiki Lounge', 'Zooper']
names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler']

print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)

print(binary_search(businesses, 'Pizzeria'))
print(binary_search(businesses, 'Apple Store'))
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77))
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89))
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5))
print(binary_search(names, 'Peter'))
print(binary_search(names, 'Tyler'))

"""
The Launch School answer is more elegant and less complex IMO, because it does 
not need recursive calling. It just remembers the index numbers it has searched. 

def binary_search(lst, search_item):
    high = len(lst) - 1
    low = 0

    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == search_item:
            return mid
        elif lst[mid] < search_item:
            low = mid + 1
        else:
            high = mid - 1

    return -1
"""