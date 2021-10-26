x, y = float(input()), float(input())


def isPointSquare(x, y):
    return x + y <= 1 and x + y >= -1 and x - y <= 1 and x - y >= -1


if isPointSquare(x, y):
    print('YES')
else:
    print('NO')
