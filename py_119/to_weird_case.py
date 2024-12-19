"""
Problem: Given a string, convert every 2nd character of every 3rd word to uppercase

Requirements:
- Leave other characters as they are
- For every 3rd word, every 2nd character is capitalized (i.e. char in index 1, 3, 5 etc.)
- Looks like it's odd indices (start lower, then upper, then lower etc.)

Questions:
- What to do with special characters / non words?

Input/Output = Strings

Data Structures:
- Since we are working with index spacing, might be better to convert to lists since strings are harder to work with 
- Final result needs to be string

Algorithm:
- We need to first identity every 3rd word
- Then every 2nd character in this word
- Sounds like we can use 2 separate functions

Every 2nd Character:
1. Given a string word, convert it to a list using list()
    a. Create a variable word = list(string)
2. Iterate through the indexes using range(len(word))
    a. If index % 2 != 0, then word[index] = word[index].upper()
2. return ''.join(word)

Every 3rd Word:
1. Given a string sentence
    a. Create a variable sentence = string.split()
2. Iterate through sentence using range(len(sentence))
    a. If (index + 1) % 3 == 0 then 
    b. new_word = weird_upper(sentence[index])
    c. sentence[index] = new_word
3. return ' '.join(sentence)
"""

def weird_upper(string):
    word = list(string)
    for i in range(len(word)):
        if i % 2 != 0:
            word[i] = word[i].upper()
    return ''.join(word)

def to_weird_case(string):
    sentence = string.split()
    for i in range(len(sentence)):
        if (i + 1) % 3 == 0:
            new_word = weird_upper(sentence[i])
            sentence[i] = new_word
    return ' '.join(sentence)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)