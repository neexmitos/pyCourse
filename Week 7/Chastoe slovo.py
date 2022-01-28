inFile = open('input.txt')
qantWords = {}
resList = []
tValue = 0
for line in inFile:
    words = line.split()
    for word in words:
        qantWords[word] = qantWords.get(word, 0) + 1
sortedQWords = sorted(qantWords.items(), key=lambda x: x[1], reverse=True)
qantWords = dict(sortedQWords)
for key in qantWords:
    if qantWords[key] >= tValue:
        resList.append([key, qantWords[key]])
        tValue = qantWords[key]
resList.sort()
print(resList[0][0])
