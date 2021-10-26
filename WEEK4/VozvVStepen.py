def power(a, n, k):
    if n == 0:
        print(1)
    elif n != 1:
        n -= 1
        a = a * k
        power(a, n, k)
    else:
        print(a)


a = float(input())
n = int(input())
k = a
power(a, n, k)
