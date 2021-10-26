rate = int(input())
rub = int(input())
kop = int(input())
years = int(input())
i = 0
kop1 = kop / 100
sum = rub + kop1
percents = 0
while i < years:
    percents = (sum * rate) / 100
    sum = percents + sum
    sumR = int(sum)
    sumK = (sum - sumR) + (5 * 10 ** -6)
    sumKRes = int(sumK * 100)
    sum = sumR + (sumKRes / 100)
    i += 1
print(sumR, sumKRes)
