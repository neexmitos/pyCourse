string = str(input())
pos = string.find(' ')
word1 = string[:pos]
word2 = string[pos + 1:]
print(word2, word1, sep=' ')
