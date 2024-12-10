def transpose(matrix):
    # First create the shell of the new matrix
    new_matrix = []
    cols = len(matrix[0])
    rows = len(matrix)
    
    for _ in range(cols):
        new_matrix.append([])
    
    # Then append the elements
    for inner in range(rows):
        for outer in range(cols):
            new_matrix[outer].append(matrix[inner][outer])
    
    return new_matrix


# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)

"""
Some really pythonic answers:

def transpose(matrix: list):
    return [list(row) for row in zip(*matrix)]
    
def transpose(matrix):
    return [[sub[i] for sub in matrix] for i in range(len(matrix[0]))]
"""