numList = list(map(int, input().split()))
count = 0
for i in range(1, len(numList) - 1):
    if numList[i] > numList[i + 1] and numList[i] > numList[i - 1]:
        count += 1
print(count)
