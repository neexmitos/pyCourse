numList = list(map(int, input().split()))
count = 0
for i in numList:
    if numList[0] <= (numList[len(numList) - 1]) and i > numList[count - 1]:
        print(i, end=' ')
    count += 1
