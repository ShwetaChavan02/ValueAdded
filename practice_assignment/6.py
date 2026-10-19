# lowest commmon multiple of two numbers LCM
# You are given two integers n1 and n2.
# Your task is to find the Lowest Common Multiple (LCM) of the two given numbers.
# The LCM of two integers is the smallest positive integer that is divisible by both integers.

def lcm(n1, n2):
    i = max(n1, n2)
    while True:
        if i % n1 == 0 and i % n2 == 0:
            return i
        i += 1