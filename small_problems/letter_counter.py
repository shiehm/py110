"""
Requirements:
- Seems like the lengths need to be in the order they are found 


Algorithm:
1. Split words in string into list string_split
2. Get a list of word lengths in a list called string_lengths
3. Iterate through this list and find the number of times each word lengths appears
    a. only count each unique word length once
"""

def string_lengths(string):
    string_split = string.split()
    string_lengths = [len(word) for word in string_split]
    return string_lengths
    
def word_sizes(string):
    word_sizes = string_lengths(string)
    word_sizes_dict = dict()
    for length in word_sizes:
        if length not in word_sizes_dict:
            word_sizes_dict[length] = word_sizes.count(length)
    return word_sizes_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

"""
Modified to count only letters
"""

def alpha_only(string):
    new_string = ''
    for char in string:
        if char.isalpha():
            new_string += char
    return new_string

def string_lengths_alpha(string):
    string_split = string.split()
    alpha_string = [alpha_only(word) for word in string_split]
    string_lengths = [len(word) for word in alpha_string]
    return string_lengths
    
def word_sizes_alpha(string):
    word_sizes = string_lengths_alpha(string)
    word_sizes_dict = dict()
    for length in word_sizes:
        if length not in word_sizes_dict:
            word_sizes_dict[length] = word_sizes.count(length)
    return word_sizes_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes_alpha(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes_alpha(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes_alpha(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes_alpha(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes_alpha('') == {})


"""
I found this to be an elegant solution
"""

def new_word_sizes(string):
    hashmap = {}

    for word in string.split():
        clean = ''.join(char for char in word if char.isalpha())
        length = len(clean)
        hashmap[length] = hashmap.get(length, 0) + 1

    return hashmap

string = 'Humpty Dumpty sat on a w@ll'
print(new_word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})