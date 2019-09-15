"""
ID: tony
LANG: PYTHON3
PROG: ride
"""
with open('ride.in') as f: 
    contents = f.read()
    a = contents.split('\n')
code = a[0]
group = a[1]
code = code.upper()
group = group.upper()
sum_code = 1
sum_group = 1
for i in range(len(code)):
    sum_code *= ord(code[i]) - 64
print (sum_code)
for i in range(len(group)):
    sum_group *= ord(group[i]) - 64
print(sum_group)
if sum_code % 47 == sum_group % 47:
    str_out = 'GO'
else: 
    str_out = 'STAY'
fout = open ('ride.out', 'w')
fout.write(str_out+'\n')