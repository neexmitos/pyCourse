rubCost = int(input())
kopCost = int(input())
pies = int(input())

rubToKop = rubCost * 100
fullCost = (rubToKop + kopCost) * pies
print(fullCost // 100, fullCost % 100)
