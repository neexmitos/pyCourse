inFile = open('input.txt', 'r', encoding='utf-8')
school = [0] * 100
for line in inFile:
    schoolnum = int(line.split()[-2])
    school[schoolnum] += 1
maxi = max(school)
for i in range(len(school)):
    if school[i] == maxi:
        print(i, end=' ')
