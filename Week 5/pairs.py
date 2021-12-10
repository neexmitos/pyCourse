l = list(map(int, input().split()))
ind = 0
check = 0
while ind < len(l):
    for i in range(0, len(l)):
        if l[ind] == l[i]:
            check += 1
    ind += 1
print(int((check - len(l)) / 2))
