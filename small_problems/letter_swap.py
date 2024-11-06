"""
Problem: Given a string of words separated by spaces, 
write a function that swaps the first and last letters of every word.

Explicit Requirements:
- You may assume that every word contains at least one letter
- the string will always contain at least one word
- each string contains nothing but words and spaces
- there are no leading, trailing, or repeated spaces.

Implicit Requirements:
- case matters
- it's always a string, return a new string

Input: String
Output: New String

Algorithm:
- Split the string up into a list of strings, seperated by spaces
- Iterate through each word-string, swapping the last index position with the first
- Join the new list with ' ' and save as a string to a variable
- Return this string
"""

def swap(string):
    words = string.split()
    new_words = []
    for word in words:
        if len(word) == 1:
            new_words.append(word)
        else:
            swap_word = word[-1] + word[1:-1] + word[0]
            new_words.append(swap_word)
    new_string = ' '.join(new_words)
    return new_string

print(swap('Oh what a wonderful day it is'))
print(swap('Abcde'))
print(swap('a'))

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

"""
The solution before breaks functions into single function pieces, 
which I think is the better way to go. Same method though for swapping. 
"""

def swap(words):
    words_list = words.split()

    for idx in range(len(words_list)):
        words_list[idx] = swap_first_last_characters(words_list[idx])

    return ' '.join(words_list)

def swap_first_last_characters(word):
    if len(word) == 1:
        return word

    return word[-1] + word[1:-1] + word[0]