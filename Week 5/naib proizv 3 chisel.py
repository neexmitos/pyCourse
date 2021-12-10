l = list(map(int, input().split()))
l1 = l.copy()
if len(l) <= 3:
    print(*l)
else:
    maxi = max(l)
    l.remove(maxi)
    maxi1 = max(l)
    l.remove(maxi1)
    maxi2 = max(l)
    mini = min(l1)
    l1.remove(mini)
    mini1 = min(l1)
    if mini * mini1 * maxi > maxi * maxi1 * maxi2:
        print(mini, mini1, maxi)
    else:
        print(maxi, maxi1, maxi2)
