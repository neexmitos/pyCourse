n = int(input())


def flag(n):
    up = '+___ '
    cent1 = '|__\\ '
    down = '|    '
    a, b, c, d = '', '', '', ''
    for i in range(1, n + 1):
        a += up
        b += f'|{i} / '
        c += cent1
        d += down
    return a, b, c, d


print(*flag(n), sep='\n')
