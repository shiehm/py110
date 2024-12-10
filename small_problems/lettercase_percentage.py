import string

def letter_percentages(letters):
    length = len(letters)
    lowercase = 0
    uppercase = 0
    neither = 0
    for letter in letters:
        if letter in string.ascii_lowercase:
            lowercase += 1
        elif letter in string.ascii_uppercase:
            uppercase += 1
        else:
            neither += 1

    result = {}
    result['lowercase'] = f'{lowercase / length * 100:.2f}'
    result['uppercase'] = f'{uppercase / length * 100:.2f}'
    result['neither'] = f'{neither / length * 100:.2f}'
    return result

def letter_percentages(letters):
    lowercase = [letter for letter in letters if letter in string.ascii_lowercase]
    uppercase = [letter for letter in letters if letter in string.ascii_uppercase]
    neither = [letter for letter in letters if letter not in lowercase and letter not in uppercase]
    length = len(letters)
    
    result = {}
    result['lowercase'] = f'{len(lowercase) / length * 100:.2f}'
    result['uppercase'] = f'{len(uppercase) / length * 100:.2f}'
    result['neither'] = f'{len(neither) / length * 100:.2f}'
    return result

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123'))
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef'))
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123'))
print(letter_percentages('123') == expected_result)