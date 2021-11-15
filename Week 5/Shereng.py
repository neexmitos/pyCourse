l = list(map(int, input().split()))
x = int(input())
insInd = 0
countIf = 1
count = 1
for i in l:
    if x % i < x and x % i != 0:
        countIf += 1
    count += 1
insInd = (count - countIf) + 1
print(insInd)
