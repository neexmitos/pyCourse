inFile = open('input.txt', 'r', encoding='utf-8')
abits = []
results = []
lastAvailable = 0
firstNavailable = 1
count = 0
scoreSum = 0
fileCount = 0
places = 0
for line in inFile:
    if fileCount == 0:
        places = int(line)
    else:
        abits = line.split()
        if int(abits[-1]) > 39 and int(abits[-2]) > 39 and int(abits[-3]) > 39:
            scoreSum = int(abits[-1]) + int(abits[-2]) + int(abits[-3])
            results.append(scoreSum)
    fileCount += 1
results.sort(reverse=True)
for result in results:
    count += 1
    if count == places:
        lastAvailable = result
    elif count == places + 1:
        firstNavailable = result
if len(results) <= places:
    print(0)
elif results.count(max(results)) > places:
    print(1)
elif len(results) > 2 and lastAvailable == firstNavailable:
    print(results[results.index(firstNavailable) - 1])
else:
    print(lastAvailable)
