a, b = int(input()), int(input())
for i in range(a, b + 1):
    if str(i)[0:2] == str(i)[4:1:-1]:
        print(i)
