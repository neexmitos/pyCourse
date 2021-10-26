num = int(input())
num1 = num
i = 0
while num != 0:
    num1 = num
    num = int(input())
    if num > num1:
        i += 1
print(i)
