numList = list(map(int, input().split()))
k = int(input())
for i in range(k + 1, len(numList)):
    numList[i], numList[k] = numList[k], numList[i]
    k += 1
numList.pop()
print(*numList)
