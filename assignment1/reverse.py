# you are given an integer n
# your task is to return the integer formed by placing the digits of n in reverse order
# note that the result should not have any leading zeros

def reverse(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num

# def reverseInteger(n):
#     return int(str(n)[::-1]  )