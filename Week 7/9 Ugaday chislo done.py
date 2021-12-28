inFile = open('input.txt', 'r', encoding='utf-8')
maxNum = int(inFile.readline().split()[0])
tempList = []
listYes = set(range(1, maxNum + 1))
listNo = set()
for line in inFile:
    tempList += (line.split('\n'))
inFile.close()
tempList = list(filter(None, tempList))
for i in range(len(tempList) - 1):
    if tempList[i + 1] == 'YES':
        listYes &= set(map(int, tempList[i].split()))
    elif tempList[i + 1] == 'NO':
        listNo |= set(map(int, tempList[i].split()))
print(*sorted(listYes - listNo))
