"""
Problem: Transpose the matrix (swap rows and columns)
Input: 2 dimensional list
Output: 2 dimensional list with rows and columns values swapped

Notes:
- We basically want a new list of lists, where the inner lists are all the values
  in the same index position of the various lists (i.e. a list of current index 0,
  1, and 2 in separate lists.)
- Made the first attempt assuming it'll be 3x3 but refactored for nxn

ALgorithm
1. Create an outer list
2. Count the number of elements in the inner list (any will do)
3. Append an empty list to the outer list for each element (using range)
4. Itereate through the original inner lists, appending each index to each new list
"""

# def transpose(matrix):
#     trans1 = list()
#     trans2 = list()
#     trans3 = list()
#     for lst in matrix:
#         trans1.append(lst[0])
#         trans2.append(lst[1])
#         trans3.append(lst[2])
#     return [trans1, trans2, trans3]

def transpose(matrix):
    # First create the shell of the new matrix
    new_matrix = []
    size = len(matrix[0])
    for _ in range(size):
        new_matrix.append([])
    
    # Then append the elements
    for inner in range(size):
        for outer in range(size):
            new_matrix[outer].append(matrix[inner][outer])
    
    return new_matrix

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True