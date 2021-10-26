from math import sqrt
x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())


def length(x1, y1, x2, y2, x3, y3):
    side1 = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    side2 = sqrt(((x2 - x3) ** 2) + ((y3 - y2) ** 2))
    side3 = sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2))
    length = side1 + side2 + side3
    return length


print(length(x1, y1, x2, y2, x3, y3))
