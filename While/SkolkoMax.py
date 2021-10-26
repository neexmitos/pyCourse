num = -1
max = -1
i = 1
while num != 0:
    num = int(input())
    if num > max:
        max = num
        i = 1
    elif num == max:
        i += 1
print(i)
