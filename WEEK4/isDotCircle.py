x, y = float(input()), float(input())
xc, yc = float(input()), float(input())
r = float(input())


def isPointInCircle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


if isPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
