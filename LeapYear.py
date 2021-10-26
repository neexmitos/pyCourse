num = int(input())
num4 = (num % 4)
num100 = (num % 100)
num400 = (num % 400)
if num4 == 0 and num100 != 0:
    print('YES')
elif num400 == 0:
    print('YES')
else:
    print('NO')
