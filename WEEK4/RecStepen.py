def power(a, n):
    c = 0
    b = a
    if n != 0:
        n -= 1
        c = b * c
        power(a, n)
        print(a)


a = int(input())
n = int(input())
power(a, n)
