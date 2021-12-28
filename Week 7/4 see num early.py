numList = list(map(int, input().split()))
numSet = set()
for num in numList:
    if num in numSet:
        print('YES')
    else:
        print('NO')
    numSet.add(num)
