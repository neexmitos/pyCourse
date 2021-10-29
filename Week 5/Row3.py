n = int(input())
k = 10 ** n - 1
y = k // 10 - 1
for i in range(k, y + 1, -2):
    print(i, end=' ')
