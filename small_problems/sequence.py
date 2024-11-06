def sequence(count, starting):
    sequence = list()
    for i in range (1, count + 1):
        sequence.append(i * starting)
    return sequence

def sequence(count, starting):
    return [i * starting for i in range (1, count + 1)]

print(sequence(5, 1))
print(sequence(4, -7))
print(sequence(3, 0))
print(sequence(0, 1000000))

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True