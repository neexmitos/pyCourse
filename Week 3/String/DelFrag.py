string = str(input())
length = len(string)
pos = string.find('h')
gnirts = string[::-1]
sop = gnirts.find('h')
pos2 = length - (sop + 1)
print(string[0:pos], string[pos2 + 1:], sep='')
