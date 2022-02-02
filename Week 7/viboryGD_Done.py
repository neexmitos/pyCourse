inFile = open('input.txt', encoding='UTF8')
parties, scoresDict = {}, {}
sumScore, allScores = 0, 0
for line in inFile:
    if line != '\n':
        parties[' '.join(line.split()[0:-1])] = line.split()[-1]
        allScores += int(line.split()[-1])
inFile.close()
electPriv = allScores / 450
for party in parties:
    parties[party] = int(parties[party]) / electPriv
    scoresDict[party] = [int(parties[party]), parties[party] % 1]
    sortSDict = sorted(scoresDict.items(), key=lambda x: (-x[1][1]))
    scoresDict = dict(sortSDict)
sumScore = sum(i[0] for i in scoresDict.values())
for key, value in scoresDict.items():
    if sumScore < 450:
        scoresDict[key] = [value[0] + 1, value[1]]
        sumScore += 1
for key, value in parties.items():
    print(key, scoresDict[key][0])
