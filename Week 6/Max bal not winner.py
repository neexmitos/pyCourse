inFile = open('input.txt', 'r', encoding='utf-8')
tempPupils = []
pupils = []
nine, ten, eleven = [], [], []
countN, countT, countE = 0, 0, 0


class School:
    name = ''
    surname = ''
    cl = 0
    score = 0


for pupil in inFile:
    tempPupils = pupil.split()
    sch = School()
    sch.name = tempPupils[1]
    sch.surname = tempPupils[0]
    sch.cl = int(tempPupils[2])
    sch.score = int(tempPupils[3])
    pupils.append(sch)
pupils.sort(key=lambda pupils: (pupils.cl, pupils.score))
for pupil in pupils:
    if pupil.cl == 9:
        nine.append(pupil.score)
    elif pupil.cl == 10:
        ten.append(pupil.score)
    else:
        eleven.append(pupil.score)
mN = max(nine)
nineNew = nine.copy()
nineNew.sort(reverse=True)
for n in nineNew:
    if mN == n:
        nine.remove(mN)
    mN = max(nine)
mT = max(ten)
tenNew = ten.copy()
for t in tenNew:
    if mT == t:
        ten.remove(mT)
    mT = max(ten)
mE = max(eleven)
elevenNew = eleven.copy()
for e in elevenNew:
    if mE == e:
        eleven.remove(mE)
    mE = max(eleven)

        # for i in ten:
#     tempT = max(ten)
#     if tempT == i:
#         countT += 1
# for i in eleven:
#     tempE = max(eleven)
#     if tempE == i:
#         countE += 1
print(*nine, *ten, *eleven)
