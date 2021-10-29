n = int(input())
myTuple = ()
for i in range(1, n + 1):
    a = str(i)
    myTuple += a,
    print(*myTuple, sep='')
