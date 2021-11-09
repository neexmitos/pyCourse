numList = list(map(int, input().split()))
oddlist = []
count = 0
for i in range(0, len(numList)):
    if numList[i] % 2 == 1:
        oddlist += [numList[i]]
min = oddlist[0]
for y in range(0, len(oddlist)):
    if oddlist[y] < min:
        min = oddlist[y]
print(min)
