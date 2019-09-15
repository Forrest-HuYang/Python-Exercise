"""
ID: tony_hu1
PROG: gift1
LANG: PYTHON3
"""
a = []
money = {}
list_friends = []
for line in open('gift1.in'):
    a.append(line.rstrip())
num_friends = int(a[0])
del a[0]
for i in range(num_friends):
    money[a[0]] = 0
    list_friends.append(a[0])
    del a[0]
while len(a) > 0:
    give_data = a[1].split(' ')
    amount = int(give_data[0])
    number = int(give_data[1])
    if int(give_data[0]) != 0:
        give_residue = amount % number
        give_money = amount // number
        money[a[0]] = money[a[0]] - amount + give_residue
        del a[0]
        del a[0]
        for i in range(number):
            money[a[0]] += give_money
            del a[0]
    else:
        for i in range(number+2):
            del a[0]
print (money)
fout = open ('gift1.out', 'w')
for i in range(num_friends):
    name = list_friends[i]
    fout.write(name + ' ' + str(money[name]) +'\n')
    
    