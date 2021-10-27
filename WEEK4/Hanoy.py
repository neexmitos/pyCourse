def move(n, i, k):
    if n == 1:
        print(1, i, k)
    else:
        tmp = 6 - i - k
        move(n - 1, i, tmp)
        print(n, i, k)
        move(n - 1, tmp, k)


n = int(input())
i = 1
k = 3
move(n, i, k)
