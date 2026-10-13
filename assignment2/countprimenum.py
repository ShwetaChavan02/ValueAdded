# count prime numbers till n

def countPrimes(n):
    count = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            isPrime = True
            if i % j == 0:
                isPrime = False
                break
        if isPrime :
            count += 1
    return count    
            