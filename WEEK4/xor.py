x, y = int(input()), int(input())


def xor(x, y):
    return (x + y <= 1) and (x == 1 or y == 1)


if xor(x, y):
    print('1')
else:
    print('0')
