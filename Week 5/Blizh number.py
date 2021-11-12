n = int(input())
l = list(map(int, input().split()))
x = int(input())
l1 = []
a = 0
cY = 0
for i in l:
    l1.append(x - i)
for y in l1:
    if y < 0:
        a = y * - 1
        l1[cY] = a
    cY += 1
min = l1[0]
minInd = 0
for y in range(0, len(l1)):
    if l1[y] < min:
        min = l1[y]
        minInd = y
print(l[minInd])
