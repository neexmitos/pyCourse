manSize = int(input())
sizeRange = list(map(int, input().split()))
sizeRange.sort()
manRange = []
countSize = 0
for i in sizeRange:
    if i >= manSize:
        manRange.append(i)
if len(manRange) >= 1:
    x = manRange[0]
for i in range(0, len(manRange)):
    if manRange[i] >= x + 3:
        x = manRange[i]
        countSize += 1
if len(manRange) == 1:
    print(1)
elif len(manRange) < 1:
    print(countSize)
else:
    print(countSize + 1)
