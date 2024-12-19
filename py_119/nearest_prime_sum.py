"""
Problem: 
- Given a list of integers 
- determine the minimum integer value that can be appended to the list 
    - so the sum of all the elements equal 
    - the closest prime number that is greater than the current sum of the numbers. 

Examples:
- the numbers in [1, 2, 3] sum to 6. 
    - The nearest prime number greater than 6 is 7. 
    - Thus, we can add 1 to the list to sum to 7.

Notes:
- The list will always contain at least 2 integers.
- All values in the list must be positive (> 0).
- There may be multiple occurrences of the various numbers in the list.

Algorithm:
Split into separate functions
- Find the closest prime number > current sum of numbers 

1. Determine the sum of the lst --> total = sum(lst)
2. Find next prime numbers:
    - Prime numbers are > 1 and can only be divisible by itself and one 
    - Sounds like a job for iteration, can add 1 to the total and test a condition is_prime() 
    a. Initialize a next_prime variable
    b. Start with the total + 1 (because we want the next largest)
    c. Test if this number is prime, if not + 1
    d. Once a number is_prime, save it as next_prime
3. Return next_prime - total
    - We can then take this prime number and subtract the current sum to get the min int 

is_prime():
1. Given a number, generate a list of numbers between 1 (exclusive) and itself (exclusive)
    a. range(2, num)
2. Use a list to generate divisors of num --> divisors = [x for x in range(2, num) if num % x == 0]
3. Return not divisors 
"""

def is_prime(num):
    divisors = [x for x in range(2, num) if num % x == 0]
    return not divisors

def nearest_prime_sum(lst):
    total = sum(lst)
    next_prime = total + 1
    while not is_prime(next_prime): 
        next_prime += 1
    return next_prime - total

# Test is_prime():
# for num in range(20):
#     print(num, is_prime(num))

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)