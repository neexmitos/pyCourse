freeSpace, users = map(int, input().split())
archList = []
count = 0
for i in range(users):
    userArch = int(input())
    archList.append(userArch)
archList.sort()
sum = 0
if len(archList) > 1:
    while sum <= freeSpace and count < len(archList):
        sum += archList[count]
        if sum > freeSpace:
            break
        count += 1
    print(count)
elif archList[0] <= freeSpace:
    print(1)
else:
    print(0)
