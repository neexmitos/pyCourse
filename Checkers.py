a = int(input())
b = int(input())
x = int(input())
y = int(input())
devab = (a + b) % 2
devxy = (x + y) % 2
if y > b:
    if devab == devxy and (x + y) >= (a + b):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
