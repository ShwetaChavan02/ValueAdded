# Check if the Number is Armstrong
# You are given an integer n. 
# You need to check whether it is an Armstrong number or not. 
# Return true if it is an Armstrong number, otherwise return false.
# An Armstrong number is a number which is equal to the sum of the digits of the number, 
# raised to the power of the number of digits.

def isArmstrong(n):
    temp = n
    digit1 = len(str(n))
    total = 0
    while temp > 0:
        digit2 = temp % 10
        total += digit2 ** digit1
        temp //= 10
    return total == n