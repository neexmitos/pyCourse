num = -1
max = -1
max1 = -1
while num != 0:
    num = int(input())
    if num >= max:
        max1, max = max, num
    elif num > max1:
        max1 = num
print(max1)
