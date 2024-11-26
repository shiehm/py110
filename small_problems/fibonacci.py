"""
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2) (where n > 2)
"""
# Recursive function:
def recursive_fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Proceedural function:
def proceedural_fibonacci(n):
    """
    1. If n = 1, return 1
    2. If n = 2, return 1
    3. If n > 2, then 
        3a. add the prior 2 together
        3b. replace the 2nd prior with the 1st prior
        3c. replce the 1st prior with the current figure
    """
    if n <= 2:
        return 1
    
    prior2 = 1
    prior1 = 1
    current = 0
    for _ in range(3, n + 1):
        current =  prior1 + prior2
        prior2 = prior1
        prior1 = current
    
    return current

# Launch School Proceedural Answer
def ls_fibonacci(n):
    """
    Only difference is not using a prior2
    """
    if n <= 2:
        return 1
    
    prior, current = 1, 1
    for _ in range(3, n + 1):
        prior, current =  current, prior + current
        
    return current


# Memoization Recursive function:
#   You won't need to call the n - 2 recursion because 
#   it will already be stored from doing the n - 1 recursion 

fibs = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n <= 2:
        return 1
    elif fibs.get(n):
        return fibs[n]
    else:
        fibs[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fibs[n]

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

"""
Can test using a while loop, as in while a len counter < input, + 1 
"""
import sys

def find_fibonacci_index_by_length(digits):
    sys.set_int_max_str_digits(50_000)
    
    result = 0
    fib = 0
    while len(str(result)) < digits:
        fib += 1
        result = fibonacci(fib)
    return fib

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print('Long Answer:')
print(find_fibonacci_index_by_length(10000) == 47847)

"""
Launch School answer calculates fibonaccis iteratively rather than calling 
the recursive function we made:


def find_fibonacci_index_by_length(length):
    sys.set_int_max_str_digits(50_000)
    first = 1
    second = 1
    count = 2

    while len(str(second)) < length:
        first, second = second, first + second
        count += 1

    return count
"""
