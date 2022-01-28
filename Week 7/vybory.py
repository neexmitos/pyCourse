inFile = open('input.txt')
sumScore = 0
candidats = set()
presidents = {}
for pres in inFile:
    candidats.add(pres.split()[0])
    president = pres.split()[0]
    score = int(pres.split()[1])
    if president not in presidents:
        presidents[president] = []
    presidents[president].append(score)
for can in sorted(candidats):
    print(can, sum(presidents[can]))
