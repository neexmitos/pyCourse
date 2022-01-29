inFile = open('input.txt', encoding='UTF8')
parties = {}
allScores = 0
for line in inFile:
    partyName = ' '.join(line.split()[0:-1])
    partyScore = line.split()[-1]
    parties[partyName] = partyScore
for party in parties:
    allScores += int(parties[party])
electPriv = allScores / 450
for party in parties:
    print(party, round(int(parties[party]) / electPriv))
