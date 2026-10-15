# Count Odd Digits
# You are given an integer n. 
# Your task is to return the number of odd digits present in the number. 
# The number will have no leading zeroes, except when the number is 0 itself.

def countodddigit(n):
    if n == 0:
        return 0
    count = 0
    while n != 0:
        digit = n % 10
        if digit % 2 != 0:
            count += 1
        n = n // 10
    return count