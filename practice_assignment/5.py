# find divisor of a number
# You are given an integer n. 
# Your task is to find all the divisors of n and return them in a sorted array.
# A number which completely divides another number is called its divisor.

def findDivisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors