"""
Write a function that takes a string argument and returns a list of substrings 
of that string. Each substring should begin with the first letter of the word, 
and the list should be ordered from shortest to longest.
"""

# def leading_substrings(string):
#     substrings = []
#     for i in range(len(string)):
#         substrings.append(string[:i + 1])
#     return substrings

def leading_substrings(string):
    return [string[:i + 1] for i in range(len(string))]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

"""
Write a function that returns a list of all substrings of a string. Order the returned list 
by where in the string the substring begins. This means that all substrings that start at 
index position 0 should come first, then all substrings that start at index position 1, and 
so on. Since multiple substrings will occur at each position, return the substrings at a 
given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:
"""

def substrings(string):
    substrings = []
    for i in range(len(string)):
        substrings.extend(leading_substrings(string[i:]))
    return substrings

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]
print(substrings('abcde'))
print(substrings('abcde') == expected_result)  # True

"""
Write a function that returns a list of all palindromic substrings of a string. 
That is, each substring must consist of a sequence of characters that reads the 
same forward and backward. The substrings in the returned list should be sorted 
by their order of appearance in the input string. Duplicate substrings should be 
included multiple times.

You may (and should) use the substrings function you wrote in the previous exercise.

For the purpose of this exercise, you should consider all characters and pay attention 
to case; that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not. In addition, 
assume that single characters are not palindromes.

Algorithm:
1. Use the prior substring functions to create a list of all substrings 
2. Reverse the string and create a list of all revers substrings 
3. Select the substrings in the forward list that are also in the reverse
4. Return this new list 

What I actually did:
1. Use prior substring function to create a list of all substrings > 1 char
2. Iterate through the substrings: if same forward and back, add to new list
3. Return the new list 
"""

def palindromes(string):
    selected_substrings = [x for x in substrings(string) if len(x) > 1]
    
    palindromes = []
    for i in range(len(selected_substrings)):
        if selected_substrings[i] == selected_substrings[i][::-1]:
            palindromes.append(selected_substrings[i])
    
    return palindromes

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True

"""
The LS solution is elegant, it separates the testing for palindrome from 
the rest of the function, which makes more sense. That way we can just do
a list comprehension selecting only palindromes from all the substrings 

def is_palindrome(word):
    return len(word) > 1 and word == word[::-1]

def palindromes(s):
    return [substring
            for substring in substrings(s)
            if is_palindrome(substring)]
"""

