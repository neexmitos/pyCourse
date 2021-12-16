myList = map(int, input().split())


def CountSort(newList):
    countList = [0] * 101
    for count in newList:
        countList[count] += 1
    for now in range(len(countList)):
        for i in range(countList[now]):
            print(now, end=' ')


CountSort(myList)
