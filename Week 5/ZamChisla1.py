a, b = int(input()), int(input())
l1 = 0
r2 = 0
l3 = 0
r4 = 0
for i in range(a, b + 1):
    l1 = i // 100
    r2 = i % 100
    l3 = r2 // 10
    r4 = r2 % 10
    tmpFig = str(r4) + str(l3)
    if l1 == int(tmpFig):
        print(i)


