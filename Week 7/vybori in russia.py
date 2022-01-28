inFile = open('input.txt', encoding='UTF8')
qantNames = {}
check = 0
winList = []
tValue = 0
for line in inFile:
    name = line.rstrip()
    qantNames[name] = qantNames.get(name, 0) + 1
inFile.close()
sortedQNames = sorted(qantNames.items(), key=lambda x: (-x[1], x[0]))
qantNames = dict(sortedQNames)
for name in qantNames:
    tValue += qantNames[name]
outFile = open('output.txt', 'w', encoding='UTF8')
for name in qantNames:
    if qantNames[name] > tValue / 2:
        outFile.write(name)
        check += 1
    else:
        winList.append(name)
if check == 0:
    outFile.write(winList[0] + '\n' + winList[1])
outFile.close()
