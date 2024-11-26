import string

DIGIT_WORDS = {
    'one': '1', 
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# def word_to_digit(message):
#     words = message.split()
#     new_words = [DIGIT_WORDS.get(word, word) for word in words]
#     return ' '.join(new_words)

# message = 'Please call me at five five five one two three four'
# print(word_to_digit(message))
# print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# # Should print True

def word_to_digit(message):
    words = message.split()
    for i in range(len(words)):
        word = words[i].lower()
        punctuation = words[i][-1]
        number = words[i][:-1].lower()
        
        if punctuation in string.punctuation and number in DIGIT_WORDS:
            words[i] = f'{DIGIT_WORDS[number]}{punctuation}'
        elif word in DIGIT_WORDS:
            words[i] = DIGIT_WORDS[word]
    return ' '.join(words)

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message))
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True

"""
Simpler solution though it uses map
"""

def word_to_digit_short(message):
    for word in DIGIT_WORDS:
        message = message.replace(word, DIGIT_WORDS[word])
    return message

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit_short(message))
print(word_to_digit_short(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True
