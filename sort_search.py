def input_data():
    b = input ("shit: ")
    demand = input("large number last, enter right; small number last, enter reverse：")
    c = b.split("," )
    a = []
    for i in range(0, len(c)-1):
        a.append(int(c[i]))
    return a,demand

def bubble_sort(a, demand):
    internationale = 0
    while internationale < len(a):
        s = 0
        while s + 1 < len(a) - internationale :
                if (a[s] > a [s+1] and demand == "right") or (a[s] < a [s+1] and demand == "reverse"):
                    a[s], a[s+1] = a[s+1], a[s]
                s += 1    
        internationale += 1
    return a

def binary_search(a, order):
    low = 0
    high = len(a) - 1
    guess = 0
    while a[guess] != order and low <= high:
        guess = (high + low) // 2
        if a[guess] > order:
            high = guess + 1
        else:
            low = guess - 1
    if (high - low) <= 1:
        return "not in the list"
    else:
        return guess + 1

raw_data, demand = input_data()
sorted_data = bubble_sort(raw_data, demand)
print (sorted_data)

order = int(input("Which number do you want?"))
pos = binary_search(sorted_data, order)
print("The position of",order,"is",pos)
