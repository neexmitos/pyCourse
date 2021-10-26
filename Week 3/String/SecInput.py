string = str(input())
length = len(string)
pos = string.find('f')
pos2 = string.find('f', pos + 1)
if pos != -1:
    print(pos2)
elif pos2 != -1:
    print(pos2)
elif pos == -1:
    print(-2)
