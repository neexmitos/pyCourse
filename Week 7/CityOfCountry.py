inFile = open('input.txt')
numCountry = int(inFile.readline().split()[0])
CityOfCountry = dict()
question = []
count = 0
for i in range(numCountry):
    for line in inFile:
        if count < numCountry:
            country = line.split()[0]
            cities = line.split()[1:]
            for city in cities:
                if city not in CityOfCountry:
                    CityOfCountry[city] = []
                CityOfCountry[city].append(country)
        elif count >= numCountry:
            for line in inFile:
                if line != '\n':
                    question.append(''.join(line.split()))
        count += 1
for city in question:
    print(*CityOfCountry[city])
