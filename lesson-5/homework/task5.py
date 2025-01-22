#Define a function is_prime(n) which returns True 
#if the given n (n > 0) is prime number, otherwise returns False.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    