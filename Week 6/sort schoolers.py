inFile = open('input.txt', 'r', encoding='utf-8')
tempPupils = []
pupils = []


class School:
    name = ''
    surname = ''
    score = 0


for pupil in inFile:
    tempPupils = pupil.split()
    sch = School()
    sch.name = tempPupils[1]
    sch.surname = tempPupils[0]
    sch.score = int(tempPupils[3])
    pupils.append(sch)
pupils.sort(key=lambda pupils: pupils.surname)
for pupil in pupils:
    print(pupil.surname, pupil.name, pupil.score)
