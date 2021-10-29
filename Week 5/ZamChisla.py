for i in range(10, 100):
    iL = i // 10
    iR = i % 10
    if i == (iL * iR) * 2:
        print(i)
