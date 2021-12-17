inFile = open('input.txt', 'r', encoding='utf-8')
tempPupils = []
pupils = []
nine, ten, eleven = [], [], []


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
print(max(nine), max(ten), max(eleven))
