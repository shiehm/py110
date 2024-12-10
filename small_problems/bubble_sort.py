"""
Problem: 
- A bubble sort works by making multiple passes (iterations) through a list. 
- On each pass, the two values of each pair of consecutive elements are compared. 
- If the first value is greater than the second, the two elements are swapped. 
- This process is repeated until a complete pass is made without performing any swaps. 
- At that point, the list is completely sorted.

Input: List
Output: List (Mutated)

Notes:
- You may assume that the list contains at least two elements.
- I'm assuming the list does not contain collections (i.e. only immutable elements)
- It might be easier to create a pass-through helper function that can be 
  iteratively used with each iteration of the list

Algorithm:
1. Iterate through the list, take the first element, compare it with the second
    - If the value of the first is greater swap it
    - If not, move onto the second element
    - Logic might be better served as, continue to compare current with next 
    - And stop if it needs to be swapped 
- Move to the second element (the the swapped list if it was swapped) and repeat 
- Once a pass is made without swaps, return the list 
"""

def bubble_sort(lst):
    swapped = True
    while swapped:
        comp_lst = list(lst)
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        if lst == comp_lst:
            swapped = False

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)
print(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True

"""
The Launch School answer is similar, except it uses a break combined with a 
while True to "toggle" the while loop whereas I make an explicit comparison 
with a shallow copy of the list before the run-through. The LS answer is 
probably more computationally efficient. It also uses continue to skip the rest 
of the loop, letting the "swapped" variable be the toggle of the loop. I do think 
my answer reads easier though. 

def bubble_sort(lst):
    while True:
        swapped = False
        for idx in range(1, len(lst)):
            if lst[idx - 1] <= lst[idx]:
                continue

            lst[idx - 1], lst[idx] = lst[idx], lst[idx - 1]
            swapped = True

        if not swapped:
            break
"""