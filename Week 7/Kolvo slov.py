inFile = open('input.txt')
qantWords = {}
for line in inFile:
    words = line.split()
    for word in words:
        qantWords[word] = qantWords.get(word, 0) + 1
        print(qantWords[word] - 1, end=' ')
