numList = list(map(int, input().split()))
count = 0
max = numList[0]
for i in range(0, len(numList)):
    if numList[i] > max:
        max = numList[i]
        count = i
print(max, count)
