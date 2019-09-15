b = input ("shit: ")
c = b.split("," )
a = []
for i in range(0, len(c)-1):
    a.append(int(c[i]))
internationale = 0
while internationale < len(a):
    s = 0
    while s + 1 < len(a) - internationale:
        if a[s] > a [s+1]:
            a[s], a[s+1] = a[s+1], a[s]
        s += 1
    internationale += 1
print (a)
