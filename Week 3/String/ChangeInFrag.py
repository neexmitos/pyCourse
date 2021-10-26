string = str(input())
posLeft = string.find('h') + 1
posRight = string.rfind('h')
stringLeft = string[:posLeft]
stringRight = string[posRight:]
stringCent = string[posLeft:posRight]
print(stringLeft, stringCent.replace('h', 'H'), stringRight, sep='')
