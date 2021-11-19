l = list(map(int, input().split()))
max2 = l[0]
indMax2 = 0
max = l[0]
a = 0
count = 0
for i in range(0, len(l)):
    if l[i] < 0:
        a = l[i] * -1
        l[i] = a
for i in range(0, len(l)):
    if l[i] > max:
        max = l[i]
        indMax = i
for y in range(0, len(l)):
    if l[y] < max and l[y] > max2:
        max2 = l[y]

print(max, max2)
# while countWh < len(l):
#     for i in l:
#         comp = l[countWh] * i
#
#         # ind += 1
#         print(comp)
#     countIf = countWh
#     countWh += 1

# print(*l)
