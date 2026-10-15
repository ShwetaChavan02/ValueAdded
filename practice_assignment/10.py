#Check for Perfect Number
# You are given an integer n. 
# You need to check if the number is a perfect number or not. 
# Return true if it is a perfect number, otherwise, return false.
#A perfect number is a number whose proper divisors 
# (excluding the number itself) add up to the number itself.


def isPerfect(n):
    if n <= 1:
        return False

    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n
