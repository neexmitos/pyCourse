l = list(map(int, input().split()))
x = int(input())
ind = 1
count = 1
for i in l:
    if x <= i:
        ind += 1
    count += 1
print(ind)