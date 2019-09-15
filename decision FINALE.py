demand = input("large number last, enter right; small number last, enter reverse：")
b = input ("shit: ")
c = b.split("," )
a = []
for i in range(0, len(c)-1):
    a.append(int(c[i]))
internationale = 0
while internationale < len(a):
    s = 0
    while s + 1 < len(a) - internationale:
            if a[s] > a [s+1] and demand == "right":
                a[s], a[s+1] = a[s+1], a[s]
            if a[s] < a [s+1] and demand == "reverse":
                a[s], a[s+1] = a[s+1], a[s]
            s += 1    
    internationale += 1
if demand != "right" and demand != "reverse":
    print("You didn't hear my question clearly, oh planctain brain!")
print (a)
            
