a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
t = 0
for i in range(0, 1001):
    if (i - e) != 0:
        if (a*(i**3) + b * (i**2) + c * i + d)/(i - e) == 0:
            t += 1
print(t)
