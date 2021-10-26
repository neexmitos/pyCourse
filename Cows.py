n = int(input())
a = n % 10
if (n >= 10 and n <= 20) or a == 0:
    print(n, 'korov')
elif a == 1:
    print(n, 'korova')
elif a >= 2 and a <= 4:
    print(n, 'korovy')
elif a >= 5 and a <= 9:
    print(n, 'korov')
