x, y = float(input()), float(input())


def isPointSquare(x, y):
    return x >= -1 and x <= 1 and y >= -1 and y <= 1


if isPointSquare(x, y):
    print('YES')
else:
    print('NO')
