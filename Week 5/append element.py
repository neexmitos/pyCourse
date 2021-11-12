numList = list(map(int, input().split()))
k, c = map(int, input().split())
numList.append(c)
iC = len(numList) - 1
for i in range(k, len(numList)):
    numList[i], numList[iC] = numList[iC], numList[i]
    k += 1
print(*numList)
