numList = list(map(int, input().split()))
count = 0
indNum = numList[0]
ind = 0
ind1 = 0
for i in range(0, len(numList)):
    if numList[i] > indNum:
        indNum = numList[i]
for y in numList:
    if y == indNum:
        ind1 = count
    count += 1
print(indNum, ind1)
