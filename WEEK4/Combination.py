n, k = int(input()), int(input())


def C(n, k):
    if k == n or k == 0:
        return 1
    else:
        return C(n - 1, k) + C(n - 1, k - 1)


print(C(n, k))
