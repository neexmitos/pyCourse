numList = list(map(int, input().split()))
k, c = map(int, input().split())
numList.append(c)
print(*numList)
for i in range (k + 1,len(numList)):
      numList[i], numList[k] = numList[k], numList[i]
      k += 1
print(*numList)
