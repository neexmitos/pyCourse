busStList = list(map(int, input().split()))
setBus1 = set()
setBus2 = set()
if busStList[0] < busStList[1]:
    setBus1 = set(range(busStList[0], busStList[1] + 1))
else:
    setBus1 = set(range(busStList[1], busStList[0] + 1))
if busStList[2] < busStList[3]:
    setBus2 = set(range(busStList[2], busStList[3] + 1))
else:
    setBus2 = set(range(busStList[3], busStList[2] + 1))
print(len(setBus1 & setBus2))
