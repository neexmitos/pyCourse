n = int(input())
i = 1
ex = 1
while ex <= n / 2:
    ex = 2 * ex
    i = i + 1
if n - ex == 0:
    print('YES')
else:
    print('NO')
