# Reverse an Integer
# You are given an integer n. 
# Your task is to return the integer formed by placing the digits of n in reverse order. 
# Note that the result should not have leading zeros.

def reverseInteger(n):
    return int(str(n)[::-1])