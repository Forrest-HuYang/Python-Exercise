def input_data():
    b = input ("shit: ")
    demand = input("large number last, enter right; small number last, enter reverse：")
    c = b.split("," )
    a = []
    for i in range(0, len(c)-1):
        a.append(int(c[i]))
    return a,demand
raw_data, demand = input_data()
print( raw_data )
