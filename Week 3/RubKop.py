from math import floor
x = float(input())
rub = floor(x)
a = (x - rub)
kop = (a + 0.00001) * 100
print(a, rub, int(kop))
