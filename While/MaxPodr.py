num = -1
num1 = -1
i = 0
iMax = 0
while num != 0:
    num = int(input())
    if num == num1:
        i += 1
    else:
        i = 0
    if i > iMax:
        iMax = i
    num1 = num
print(iMax + 1)
