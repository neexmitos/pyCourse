inFile = open('input.txt', 'r', encoding='utf-8')
data = list(inFile.readline().split())
n, m = int(data[0]), int(data[1])
firstSet = set()
secondSet = set()
count = 0
for line in inFile:
    if count < n:
        firstSet.add(int(line))
    else:
        secondSet.add(int(line))
    count += 1
inFile.close()
print(len(firstSet & secondSet))
print(*sorted(firstSet & secondSet))
print(len(firstSet - secondSet))
print(*sorted(firstSet - secondSet))
print(len(secondSet - firstSet))
print(*sorted(secondSet - firstSet))
