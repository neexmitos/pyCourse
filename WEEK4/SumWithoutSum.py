def sum(a, b):
    if b == 0:
        print(a)
    elif b >= 1:
        a += 1
        b -= 1
        sum(a, b)


a = int(input())
b = int(input())
sum(a, b)
