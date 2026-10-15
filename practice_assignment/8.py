# count prime numbers till n
# You are given an integer n.
# Your task is to find out the number of prime numbers in the range [1, n] (inclusive). 
# A prime number is defined as a number greater than 1 that has no divisors other than 1 and itself.

def countPrimes(n):
    count = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            isPrime = True
            if i % j == 0:
                isPrime = False
                break
        if isPrime :
            count += 1
    return count  