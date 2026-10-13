# check if a number is prime or not
# prime :  a number which is only divisible by 1 and the number itself

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True