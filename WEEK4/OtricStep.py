def power(a, n, k):
    i = 1
    if n == 0:
        return 1
    elif n > 0:
        while i < n:
            a = a * k
            i += 1
        return a
    else:
        n = n * (-1)
        while i < n:
            a = a * k
            i += 1
        a = 1 / a
        return a


a = float(input())
n = int(input())
k = a
print(power(a, n, k))
