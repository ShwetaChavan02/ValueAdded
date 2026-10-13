# you are given an integer n
# your need to check whether the number is armstrong number or not
# return True if the number is armstrong number otherwise return False

def isArmstrong(n):
    temp = n
    digit1 = len(str(n))
    total = 0
    while temp > 0:
        digit2 = temp % 10
        total += digit2 ** digit1
        temp //= 10
    return total == n