rate = int(input())
rub = int(input())
kop = int(input())
kop1 = kop / 100
sum = rub + kop1
percents = (sum * rate) / 100
sumVkl = percents + sum
rubSum = int(sumVkl)
kopSum = sumVkl - rubSum
print(rubSum, int((kopSum + 0.000001) * 100))
