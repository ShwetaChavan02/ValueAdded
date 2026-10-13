# find gcd of two  numbers
# gcd is the largest number that divided both number equally

def gcdoftwonumbers(n1, n2):
    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1