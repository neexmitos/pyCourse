numList = list(map(int, input().split()))
decr = -1
for i in range(0, len(numList) // 2):
    numList[i], numList[decr] = numList[decr], numList[i]
    decr -= 1
print(*numList)
