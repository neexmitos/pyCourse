inFile = open('input.txt', 'r', encoding='utf-8')
maxNum = int(inFile.readline().split()[0])
tempList = []
testSet = set(range(1, maxNum + 1))
firstSet = set()
secondSet = set()
for line in inFile:
    tempList.append((line.split()))
inFile.close()
tempList = list(filter(None, tempList))  # почитай про filter в курсе об этом молчат
for i in range(len(tempList) - 1):
    #     x = tempList[i + 1]
    if tempList[i + 1] == ['YES']:
        for x in tempList[i]:
            firstSet.add(int(x))  # почитай про update
    elif tempList[i + 1] == ['NO']:
        for y in tempList[i]:
            secondSet.add(int(y))  # почитай про update
if secondSet == set():
    print(*sorted(testSet - firstSet))
elif firstSet == set():
    print(*sorted(testSet - secondSet))
else:
    print(*sorted(firstSet - secondSet))
print(firstSet, secondSet)
