inFile = open('input.txt', 'r', encoding='utf-8')
txtSet = set(inFile.read().split())
print(len(txtSet))
