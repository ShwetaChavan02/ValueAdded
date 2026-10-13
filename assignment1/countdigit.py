#count all digits of a number you are given an integer n 
# you need to return the number of digits in the number

def countdigits(n):
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count