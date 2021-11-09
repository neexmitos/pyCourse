numList = list(map(int, input().split()))
decr = -1
for i in range(0, len(numList)):
    numList[i] = numList[decr]
    decr -= 1
print(numList)
