inFile = open('input.txt')
qantWords = {}
resList = []
tValue = 0
for line in inFile:
    words = line.split()
    for word in words:
        qantWords[word] = qantWords.get(word, 0) + 1
sortedQWords = sorted(qantWords.items(), key=lambda x: (-x[1], x[0]))
qantWords = dict(sortedQWords)
print(*(qantWords.keys()), sep='\n')
