# Assuming the lists are the same length, if not can find the shorter length list and use that
# Zip automatically does that 

def multiply_items(list_a, list_b):
    return [a * b for a, b in zip(list_a, list_b)]

def multiply_items(list_a, list_b):
    return [list_a[i] * list_b[i] for i in range(len(list_a))]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True