"""
Problem:
You have a number of building blocks that can be used to build a valid structure. 
There are certain rules about what determines a valid structure.

Write a program that, given the number of available blocks, calculates the number 
of blocks left over after building the tallest possible valid structure.

Inputs:
- Integer representing number of available blocks 

Outputs:
- Integer representing the number of leftover blocks

Explicit Rules:
- The building blocks are cubes & the structure is built in layers.
- The top layer is a single block.
- A block in an upper layer must be supported by four blocks in a lower layer.
- A block in a lower layer can support more than one block in an upper layer.
- You cannot leave gaps between blocks.

Implicit Rules:
- Blocks are arranged 2x2 to support the block above if it is singular: 
- Layer number correlates with number of blocks, and if it is square then layer number ^ 2 = number of blocks 

Example:
- A theoretical pyramid would look like this from top to bottom:
    - 1 cube (1x1)
    - 4 cubes (2x2)
    - 9 cubes (3x3)
    - 16 cubes (4x4)

Questions:
- How are the cubes structured to support the above layers 
(i.e. is this in a row of 4 or 2x2 supporting one in the middle? Assuming 2x2.)
- Where is the above layer placed? Assuming at the intersection of the 2x2?
- Does each layer have the same dimensions or can they have different dimentions 
(i.e. 4x2 supporting 3x1 or has to be 4x4 for 3x3? Do the below work?) 
    - 2x2 supports 1x1
    - 3x2 supports 2x1 (still supported by 4 but some blocks below is supporting more than 1)
    - 4x2 supports 3x1 
    - 4x3 supports 3x2 and so on (each base supports n-1 on each dimension)

Test Cases:
- 20 cubes would be 6 leftover 
- 25 cubes would be 11 leftover
- 30 cubes would be 0 leftover 
- 35 would be 5 leftover

leftover_blocks(20) == 6
leftover_blocks(25) == 11
leftover_blocks(30) == 0
leftover_blocks(35) == 5

Data Structures:
- We can use a list to represent the pyramid, with the index being the row (starting from 1 for top most)
- Can use list comprehension to form the pyramid

Algorithm:
1. Declare 
    a. a variable for blocks remaining and set it equal to the number of total cubes 
    b. a variable for row number and set it to 1 for the first row number 
2. Using a loop, 
    a. first test if the blocks remaining - blocks in the row will be >= 0
    b. If so, subtract the number of cubes in this row from blocks remaining 
    c. Add += 1 to the row number 
3. Return the cube amount when the loop ends 

"""

def leftover_blocks(num_blocks):
    blocks_remaining = num_blocks
    row_number = 1
    while blocks_remaining - row_number**2 >= 0:
        blocks_remaining -= row_number**2
        row_number += 1
    return blocks_remaining
    
print(leftover_blocks(20))
print(leftover_blocks(25))
print(leftover_blocks(30))
print(leftover_blocks(35))

print(leftover_blocks(0) == 0)  # True
print(leftover_blocks(1) == 0)  # True
print(leftover_blocks(2) == 1)  # True
print(leftover_blocks(4) == 3)  # True
print(leftover_blocks(5) == 0)  # True
print(leftover_blocks(6) == 1)  # True
print(leftover_blocks(14) == 0) # True