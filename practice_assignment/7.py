# GCD greatest common divisor of two numbers
# You are given two integers n1 and n2.
# Your task is to find the Greatest Common Divisor (GCD) of the two given numbers. 
# The GCD of two integers is the largest positive integer 
# that divides both of the integers without leaving a remainder.


def findGCD(n1, n2):
    i = min(n1, n2)
    while i > 0:
        if n1 % i == 0 and n2 % i == 0:
            return i
        i -= 1
