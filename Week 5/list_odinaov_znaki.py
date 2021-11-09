A = list(map(int, input().split()))
i = 0
x = 0
while i < len(A) - 1:
    if (x == 0) and \
            ((A[i] < 0 and A[i + 1] < 0) or (A[i] >= 0 and A[i + 1] >= 0)):
        print(A[i], A[i + 1])
        x += 1
    i += 1
