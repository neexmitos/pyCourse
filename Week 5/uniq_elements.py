l = list(map(int, input().split()))
l1 = l.copy()
for i in l:
    if l1.count(i) == 1:
        print(i, end=' ')
