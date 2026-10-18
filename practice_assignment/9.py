# check for prime number
# you are given integer n
# your task is to check if the number is prime or not
# a prime number is defined as number greater than 1 and has no divisors other than 1 and itself

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True