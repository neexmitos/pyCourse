n = int(input())
sum = 0
sumC = 0
card = 0
for i in range(1, n + 1):
    sum += i
for y in range(1, n):
    m = int(input())
    sumC += m
print(sum - sumC)
