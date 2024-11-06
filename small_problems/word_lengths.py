"""
Write a function that takes a string as an argument and returns 
a list that contains every word from the string, with each word 
followed by a space and the word's length. If the argument is 
an empty string or if no argument is passed, the function should 
return an empty list. You may assume that every pair of words in 
the string will be separated by a single space.

Input: String (words separated by single space)
Output: List of strings (word and length with single space)

Notes:
- Will need to count the length of each word with len()
- Will need to separate the words 
- Since a single space will separate the words, use split()
- Can build a new list that has len() of each word 
- Then combine the lists 

Algorithm:
- Helper functiont to create length list and word list 
1. Take the string as an argument and use split() 
2. Create a new list for lengths
3. Iterate through the words list and append len to length list
4. Return the word list and length list

- Function to combine the lists
1. Create an empty new list 
2. Iterate through a range that runs to the length of the word list
3. Append each index from the word list + ' ' + length list 
4. Return this list 

Note: Actually just going to do it in 1 function
- Run into edge case when it's an empty string or no argument
"""

"""
More pythonic LS answer below. Can use f strings in list comprehension.
Basically same as mine just condensed. 
"""

def word_lengths(string=''):
    return [f"{word} {len(word)}" for word in string.split()]

# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True