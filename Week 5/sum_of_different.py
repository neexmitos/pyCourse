l = list(map(int, input().split()))
prev = l[0]
count = 1
for i in l:
    if i != prev:
        prev = i
        count += 1
print(count)
