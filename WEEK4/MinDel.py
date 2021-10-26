from math import sqrt
n = int(input())


def MinDivisor(n):
    i = 2
    while n % i != 0:
        if sqrt(n) >= i:
            i += 1
        else:
            return n
    return i


print(MinDivisor(n))
