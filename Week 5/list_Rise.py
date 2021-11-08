A = list(map(int, input().split()))


def inAscending(A):
    ind = 0
    while ind < len(A) - 1 and A[ind] < A[ind + 1]:
        ind += 1
    if ind == len(A) - 1:
        return 'YES'
    else:
        return 'NO'


print(inAscending(A))
