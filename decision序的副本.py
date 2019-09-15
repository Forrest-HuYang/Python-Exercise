demand = "反"
b = 2,1,3,5,4,
def 排(demand,b):
    c = b.split("," )
    a = []
    for i in range(0, len(c)-1):
        a.append(int(c[i]))
    internationale = 0
    if demand == "正":
        while internationale < len(a):
            s = 0
            while s + 1 < len(a) - internationale:
                if a[s] <= a [s+1]:
                    s += 1
                else:
                    a[s], a[s+1] = a[s+1], a[s]
                    s += 1
            internationale += 1
    if demand == "反":
        while internationale < len(a):
            s = 0
            while s + 1 < len(a) - internationale:
                if a[s] >= a [s+1]:
                    s += 1
                else:
                    a[s], a[s+1] = a[s+1], a[s]
                    s += 1
            internationale += 1
    else:
        print("You didn't hear my question clearly, oh planctain brain!")
    print (a)
x = 排(demand,b)
print(x)
                      

            
