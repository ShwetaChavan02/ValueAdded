# Factorial of a Given Number
# You are given an integer n. 
# Return the value of n! (n factorial). 
# The factorial of a number is the product of all positive integers 
# less than or equal to that number.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i   
    return fact