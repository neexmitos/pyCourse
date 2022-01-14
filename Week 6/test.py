mySet1 = {'Russian', 'English', 'Japanese'}
mySet2 = {'Russian', 'English'}
mySet3 = {'English', 'German'}

n = mySet1 & mySet2
m = mySet1 | mySet2

print(n, m) # значение которое есть во всех 3 сетах
# print(mySet1 ^ mySet2 ^ mySet3)