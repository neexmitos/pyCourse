l = list(map(int, input().split()))
count = 0
for i in range(len(l)):
    if l[i] != 0:
        l[i], l[count] = l[count], l[i]
        count += 1
print(*l)
