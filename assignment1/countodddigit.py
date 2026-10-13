# you are given an integer n
# your task is to return the number of odd digits in the number
# the number will have no leading zerox, except when the number is 0 itself

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
