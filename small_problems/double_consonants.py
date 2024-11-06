VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def double_consonants(string):
    new_string = ''
    for char in string:
        if char not in VOWELS and char.isalpha():
            new_string += char * 2
        else:
            new_string += char
    return new_string

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")

# All of these examples should print True
print(double_consonants('String'))
print(double_consonants('Hello-World!'))
print(double_consonants('July 4th'))
print(double_consonants(''))