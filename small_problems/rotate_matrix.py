"""
Notes
- The first row becomes the last column
- The last row becomes the first column
- So it's similar to transpose where the first row becomes the first column
- Transpose is really just -90 rotation then flipped 

Example:

old_matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix [
    [3, 4, 1]
    [9, 7, 5]
    [6, 2, 8]
]

- New[0][0] == Old[2][0]
- New[1][0] == Old[2][1]
- New[2][0] == Old[2][2]

- New[0][1] == Old[1][0]
- New[1][1] == Old[1][1]
- New[2][1] == Old[1][2]

- New[0][2] == Old[0][0]
- New[1][2] == Old[0][1]
- New[2][2] == Old[0][2]
"""

def rotate90(matrix):
    # First create the shell of the new matrix
    new_matrix = []
    cols = len(matrix[0])
    rows = len(matrix)
    
    for _ in range(cols):
        new_matrix.append([])
    
    # Then append the elements
    for inner in range(rows - 1, -1, -1):
        for outer in range(cols):
            new_matrix[outer].append(matrix[inner][outer])
    
    return new_matrix

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

print(matrix1)
print(rotate90(matrix1))

print(matrix2)
print(rotate90(matrix2))

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)

"""
I like how this guy used ennumerate for grab the index and element.
Practice using ennumerate more:

def rotate90(matrix):
    new_matrix = []

    for _ in range(len(matrix[0])):
        new_matrix.append([])

    for item in matrix[::-1]:
        for idx, value in enumerate(item):
            new_matrix[idx].append(value)

    return new_matrix
"""