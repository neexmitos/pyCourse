l = list(map(int, input().split()))
min = l[0]
indMin = 0
max = l[0]
indMax = 0
for i in range(0, len(l)):
    if l[i] > max:
        max = l[i]
        indMax = i
    elif l[i] < min:
        min = l[i]
        indMin = i
l[indMax], l[indMin] = l[indMin], l[indMax]
print(*l)
