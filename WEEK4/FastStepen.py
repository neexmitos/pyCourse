def fastPower(a, n):
    if n == 0:
        return 1
    if n % 2 != 0:
        return a*fastPower(a, n - 1)
    else:
        return fastPower(a**2, n/2)


a = float(input())
n = int(input())
print(fastPower(a, n))
