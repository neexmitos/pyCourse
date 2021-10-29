from math import factorial
n = int(input())
fact = 0
count = 0
for i in range(1, n + 1):
    fact = factorial(i)
    count = count + fact
print(count)
