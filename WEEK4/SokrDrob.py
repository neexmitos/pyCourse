def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


def ReduceFraction(n, m):
    print(int(n / gcd(n, m)), int(m / gcd(n, m)))


n = int(input())
m = int(input())
ReduceFraction(n, m)
