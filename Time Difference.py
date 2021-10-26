hour1 = int(input())
min1 = int(input())
sec1 = int(input())
hour2 = int(input())
min2 = int(input())
sec2 = int(input())
hourInSec1 = hour1 * 3600
minInSec1 = min1 * 60
hourInSec2 = hour2 * 3600
minInSec2 = min2 * 60
alltime1 = hourInSec1 + minInSec1 + sec1
alltime2 = hourInSec2 + minInSec2 + sec2
print(alltime2 - alltime1)
