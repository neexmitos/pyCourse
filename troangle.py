a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    max = a
    a1 = b
    b1 = c
elif b >= a and b >= c:
    max = b
    a1 = a
    b1 = c
elif c >= a and c >= b:
    max = c
    a1 = a
    b1 = b
if max <= 0 or a1 <= 0 or b1 <= 0:
    print('impossible')
elif max >= a1 + b1:
    print('impossible')
elif max**2 == (a1**2) + (b1**2):
    print('rectangular')
elif max**2 < (a1**2) + (b1**2):
    print('acute')
elif max**2 > (a1**2) + (b1**2):
    print('obtuse')
