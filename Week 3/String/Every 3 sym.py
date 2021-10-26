string = str(input())
i = -1
pos = -1
while i < len(string):
    i += 1
    pos = i % 3
    if pos == 0:
        print(string[i+1:i+3], sep='', end='')
