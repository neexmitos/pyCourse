string = str(input())
length = len(string)
pos = string.find('h')
gnirts = string[::-1]
sop = gnirts.find('h')
pos2 = length - (sop + 1)
print(string[:pos2] + string[pos + 1:])
