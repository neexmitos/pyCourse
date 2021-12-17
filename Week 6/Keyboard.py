qKey = int(input())
qeClicks = list(map(int, input().split()))
totPress = int(input())
seqPress = list(map(int, input().split()))
baseList = [0] * (len(qeClicks) + 1)
for count in seqPress:
    baseList[count] += 1
baseList.remove(0)
for key in range(len(qeClicks)):
    if qeClicks[key] >= baseList[key]:
        print('NO')
    else:
        print('YES')
