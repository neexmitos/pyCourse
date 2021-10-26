from math import floor, ceil
x = float(input())
a = floor(x)
b = x - a
z = int(b * 100)
if z < 50:
    print(floor(x))
elif z >= 50:
    print(ceil(x))
