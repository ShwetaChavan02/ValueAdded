# lowest common multiple
# lcm : 

def lcmoftwonumbers(n1, n2):
    a = n1
    b = n2

    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r

    gcd = n1
    return (a * b) // gcd
