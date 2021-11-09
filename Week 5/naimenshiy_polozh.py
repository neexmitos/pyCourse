numList = list(map(int, input().split()))
poslist = []
for i in range(0, len(numList)):
    if numList[i] > 0:
        poslist += [numList[i]]
min = poslist[0]
for y in range(0, len(poslist)):
    if poslist[y] < min:
        min = poslist[y]
print(min)
