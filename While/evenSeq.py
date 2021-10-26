num = int
sum = 0
i = -1
while num != 0:
    num = int(input())
    devNum = num % 2
    if devNum == 0:
        i += 1
print(i)
