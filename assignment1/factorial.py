# you are given an integer n
# your task is to return the value of n!
# the factorial of a number n is the product of all positive integers less than or equal to n

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact