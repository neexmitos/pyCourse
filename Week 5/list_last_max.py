numList = list(map(int, input().split()))
count = 0
indNum = 0
for i in range(0, len(numList)):
    if numList[i] > indNum:
        indNum = numList[i]
if numList.count(indNum) > 1:
    print(indNum, numList.index(indNum, numList.index(indNum) + 1))
else:
    print(indNum, numList.index(indNum))
