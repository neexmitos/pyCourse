l = list(map(int, input().split()))
if len(l) <= 2 and l[0] < l[1]:
    print(l[0], l[1])
elif len(l) <= 2 and l[0] > l[1]:
    print(l[1], l[0])
else:
    maxi = max(l)
    l.remove(maxi)
    maxi1 = max(l)
    mini = min(l)
    l.remove(mini)
    mini1 = min(l)
    if maxi * maxi1 > mini * mini1:
        if maxi < maxi1:
            print(maxi, maxi1)
        else:
            print(maxi1, maxi)
    else:
        if mini < mini1:
            print(mini, mini1)
        else:
            print(mini1, mini)
