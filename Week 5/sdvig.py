l = list(map(int, input().split()))
l1 = l.copy()
iC = len(l) - 1
for i in range(0, len(l) - 1):
    l1[i + 1] = l[i]
l1[0] = l[iC]
print(*l1)
