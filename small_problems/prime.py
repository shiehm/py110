"""
This solution is very computationally expensive
"""
def is_prime_all(n):
    divisors = [num for num in range(1, n + 1) if n % num == 0]
    return len(divisors) == 2

"""
Another way to do it is to just test numbers up to the square root.
That way once it finds a factor that is > 1 and < the sq rt + 1, it's not prime.
It's far less expensive because it'll stop at the first factor.
"""

def is_prime(n):
    if n == 1:
        return False
    
    for num in range(2, int(n**0.5) + 1):
        if n % num == 0:
            return False
    
    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True