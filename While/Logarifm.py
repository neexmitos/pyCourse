n = int(input())
i = 1
ex = 2
if n == 1:
    print(0)
else:
    while ex < n:
        ex = ex + ex
        i = i + 1
    print(i)
