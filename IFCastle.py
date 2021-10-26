a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if d >= a and e >= b:
    print('YES')
elif d >= c and e >= b:
    print('YES')
elif d >= b and e >= a:
    print('YES')
elif e >= c and d >= b:
    print('YES')
elif e >= c and d >= a:
    print('YES')
elif e >= a and d >= c:
    print('YES')
else:
    print('NO')
