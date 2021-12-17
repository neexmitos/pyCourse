numofstuds = int(input())
outFile = open('input.txt', 'w', encoding='utf8')
studList = []
for num in range(numofstuds):
    stud = input()
    print(stud, file=outFile)
outFile.close()


class School:
    surname = ''
    score = 0


inFile = open('input.txt', 'r', encoding='utf8')
for pupil in inFile:
    tempPupils = pupil.split()
    sch = School()
    sch.surname = tempPupils[0]
    sch.score = int(tempPupils[1])
    studList.append(sch)
studList.sort(key=lambda studList: studList.score, reverse=True)
for pupil in studList:
    print(pupil.surname)
