inFile = open('input.txt', 'r', encoding='utf-8')
maxNum = int(inFile.readline().split()[0])
listOfSet = []
setEach = set()
for i in range(maxNum):
    pupil = inFile.readline()
    setPupLang = set()
    for y in range(int(pupil)):
        setPupLang.add(inFile.readline().rstrip('\n'))
    listOfSet.append(setPupLang)
setLangOfAll = listOfSet[0]
for i in range(len(listOfSet)):
    setLangOfAll &= listOfSet[i]
    setEach |= listOfSet[i]
print(len(setLangOfAll))
print(*setLangOfAll, sep='\n')
print(len(setEach))
print(*setEach, sep='\n')
