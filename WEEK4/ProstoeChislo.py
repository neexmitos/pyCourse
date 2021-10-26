from math import sqrt


def isPrime(n):
    i = 2
    if n == 2:
        return True
    while n % i != 0:
        i += 1
        if (n % i == 0) and (i <= sqrt(n)):
            return False
        elif i == sqrt(n):
            return False
        elif i > sqrt(n):
            return True
    return False


n = int(input())
if isPrime(n):
    print('YES')
else:
    print('NO')
