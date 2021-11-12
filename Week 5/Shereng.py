l = list(map(int, input().split()))
x = int(input())
l1 = []
for i in l:
    if x - i < 0:
        l1.append((x - i) * -1)
    else:
        l1.append(x - i)
min = l1[0]
minInd = 0
count = 1
zCount = 0
for y in l1:
    if y <= min:
        min = y
        minInd = count + 1
    count += 1
if x <= l[0]:
    print(minInd)
else:
    print(1)
