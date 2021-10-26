a = int(input())
b = int(input())
x = int(input())
y = int(input())
devab = (a + b) % 2
devxy = (x + y) % 2
if devab == devxy:
    print('YES')
else:
    print('NO')
