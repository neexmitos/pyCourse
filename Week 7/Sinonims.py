inFile = open('input.txt')
numSino = int(inFile.readline().split()[0])
sinonims = {}
for i in range(numSino):
    sinoList = inFile.readline().split()
    sinonims[sinoList[0]] = [sinoList[1]]
    sinonims[sinoList[1]] = [sinoList[0]]
print(*sinonims[inFile.readline().rstrip()])
