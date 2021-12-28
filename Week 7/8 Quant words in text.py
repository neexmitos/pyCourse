inFile = open('input.txt', 'r', encoding='utf-8')
txtList = []
txtSet = set()
for line in inFile:
    txtList.append(line.split())
for i in range(len(txtList)):
    for txt in txtList[i]:
        txtSet.add(txt)
print(len(txtSet))
