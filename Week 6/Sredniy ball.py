inFile = open('input.txt', 'r', encoding='utf-8')
tempPupils = []
pupils = []
nine, ten, eleven = 0, 0, 0
countNine, countTen, countEleven = 0, 0, 0


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
pupils.sort(key=lambda pupils: pupils.cl)
for pupil in pupils:
    if pupil.cl == 9:
        nine += pupil.score
        countNine += 1
    elif pupil.cl == 10:
        ten += pupil.score
        countTen += 1
    else:
        eleven += pupil.score
        countEleven += 1
print(nine / countNine, ten / countTen, eleven / countEleven)
