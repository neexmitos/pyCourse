numb = int(input())
first2numb = numb // 100
sec2Numb = numb % 100
Sec2NumbSecondDigit = sec2Numb % 10
Sec2NumbFirstDigit = sec2Numb // 10
reverseSecNumb = str(Sec2NumbSecondDigit) + str(Sec2NumbFirstDigit)
print(first2numb - int(reverseSecNumb) + 1)
