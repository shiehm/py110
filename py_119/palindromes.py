def substrings(string):
    result = []
    for start_index in range(len(string) - 2):
        for num_chars in range(2, len(string) - start_index):
            substring = string[start_index:start_index + num_chars]
            result.append(substring)
    return result

def is_palindrome(string):
    return string[::-1] == string

def palindrome_substrings(s):
    substrings_list = substrings(s)
    return [substring for substring in substrings_list if is_palindrome(substring)]

print(palindrome_substrings("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
print(palindrome_substrings("palindrome")) # []
print(palindrome_substrings(""))           # []
print(palindrome_substrings("repaper"))
# ['repaper', 'epape', 'pap']

print(palindrome_substrings("supercalifragilisticexpialidocious"))
# ["ili"]