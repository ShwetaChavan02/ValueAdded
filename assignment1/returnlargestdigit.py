# you are given an integer n
# your task is to return the largest digit in the number
def return_largest_digit(n):
    if n == 0:
        return 0
    largest_digit = 0
    while n != 0:
        digit = n % 10
        if (digit > largest_digit):
            largest_digit = digit
        n = n // 10
    return largest_digit