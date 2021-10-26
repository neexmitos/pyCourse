string = str(input())
length = len(string)
pos = string.find('f')
gnirts = string[::-1]
sop = gnirts.find('f')
pos2 = length - (sop + 1)
if pos != -1 and string.find('f', pos + 1) != -1:
    print(pos, pos2)
elif pos != -1:
    print(pos)
