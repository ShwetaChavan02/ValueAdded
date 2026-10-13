# check if a number is a perfect number

# find divisor of the number
# divisor : the remainder should be 0 when divided by the divisor

def isPerfectNumber(n):
    sum = 1
    for i in range(2, n):
        if n % i == 0:
            sum += i

    return sum == n

    
