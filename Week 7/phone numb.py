contacts = open('input.txt')
ind = -1
contList = []
for num in contacts:
    contList.append(''.join([x for x in num if x.isdigit()]))
for num in contList:
    ind += 1
    if len(num) == 7:
        contList[ind] = '495' + num
    elif num[0] == '7' or num[0] == '8':
        contList[ind] = num[1:]
newNum = contList[0]
contList.pop(0)
for num in contList:
    if num == newNum:
        print('YES')
    else:
        print('NO')
