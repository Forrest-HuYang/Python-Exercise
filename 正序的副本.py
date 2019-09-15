b = input ("shit: ")
c = b.split("," )
a = []
order = int(input("Which number do you want?"))
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
low = 0
high = a[len(a) - 1]
guess = 1
while a[guess - 1] != order:
    guess = (high + low) // 2
    if a[guess - 1] > order:
        high = guess
    if a[guess - 1] < order:
        low = guess
print (guess)
