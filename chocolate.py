n = int(input())
m = int(input())
k = int(input())
y = n * m
if (k % n == 0 or k % m == 0) and k < y:
    print('YES')
else:
    print('NO')
