def arrangement(demand,a):
    internationale = 0
    while internationale < len(a):
        s = 0
        while s + 1 < len(a) - internationale :
                if (a[s] > a [s+1] and demand == "right") or (a[s] < a [s+1] and demand == "reverse"):
                    a[s], a[s+1] = a[s+1], a[s]
                s += 1    
        internationale += 1
    return (a)
