"""
Write a program that solicits six (6) numbers from the user and prints a message 
that describes whether the sixth number appears among the first five.
"""

def simple_search():
    num1 = input('Enter the 1st number: ')
    num2 = input('Enter the 2nd number: ')
    num3 = input('Enter the 3rd number: ')
    num4 = input('Enter the 4th number: ')
    num5 = input('Enter the 5th number: ')
    num_last = input('Enter the last number: ')
    
    if num_last in [num1, num2, num3, num4, num5]:
        print(f'{num_last} is in {num1}, {num2}, {num3}, {num4}, {num5}')
    else:
        print(f'{num_last} is not {num1}, {num2}, {num3}, {num4}, {num5}')
    
"""
Suppose we alter the problem to look for a number that satisfies a condition 
(e.g., a number greater than 25) instead of a specific number? Would the 
current solution still work? Why or why not?
"""

def advanced_criteria():
    num1 = input('Choose a first number: ')
    comparison = input('Choose a comparison (<, >, <=, >=, ==): ')
    num2 = input('Choose a second numer: ')
    expression = f'{num1} {comparison} {num2}'
    print(expression, 'is', eval(expression))
    
advanced_criteria()