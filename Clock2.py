seconds = int(input())
minute = seconds // 60
hour = seconds // 3600
minute2 = minute % 60
seconds2 = seconds % 60
minute11 = minute2 % 10
seconds11 = seconds2 % 10
minute22 = minute2 // 10
seconds22 = seconds2 // 10
print(hour % 24, ':', minute22, minute11, ':', seconds22, seconds11, sep='')
