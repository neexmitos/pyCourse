string = str(input())
if len(string) == 1:
    print(string)
else:
    symbFirst = string[0]
    symbLast = string[len(string) - 1]
    stringNew = string[1:len(string) - 1]
    repStr = stringNew.replace('', '*')
    print(symbFirst + repStr + symbLast)
