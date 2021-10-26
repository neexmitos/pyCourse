a = int(input())
b = int(input())
c = int(input())
a1 = a % 2
b1 = b % 2
c1 = c % 2
if a1 != b1 or a1 != c1:
    print('YES')
else:
    print('NO')
