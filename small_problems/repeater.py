def repeater(string):
    new_string = ''
    for char in string:
        new_string += char 
        new_string += char 
    return new_string

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True