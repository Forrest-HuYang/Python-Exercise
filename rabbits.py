n = int(input("How many months since the first bunnies arrived?"))
original = 0
total = 1
i = 1
list_rabbits = [1]
newborn = [0]
while i < n:
    original, total = total, original + total
    list_rabbits.append(total)
    i += 1

print(total)
print(list_rabbits)
print(newborn)