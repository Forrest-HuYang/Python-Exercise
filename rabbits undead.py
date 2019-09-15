import easygui
n = int(easygui.enterbox("How many months since the first bunnies arrived?"))
age = int(easygui.enterbox("How many months does a bunny live?"))
age_smallbunnies = int(easygui.enterbox("When do bunnies start to give birth(months)?"))
original = 0
total = 1
i = age_smallbunnies - 1
if n < 1 or age < 1 :
    print("You're impossible")
elif age <= age_smallbunnies:
    print("You're left with no bunnies")
else:
    list_bunnies = []
    newborn = [0]
    dead = []
    for undead in range(age):
        dead.append(0)
    for lonely in range(age_smallbunnies - 1):
        list_bunnies.append(1)
    total_dead = 0

    while i < n:
        original, total = total, original + total
        if i > age - 1:
            dead.append(newborn[i - age + 2])
            total -= dead[i]
        newborn.append(total - original + dead[i])
        list_bunnies.append(total)
        i += 1

    for i in range(1,len(dead)):
        total_dead += dead[i]
    print("You've got a total of" , total , "pairs of cute little bunnies")
    print("Here's a list of how many pairs of bunnies there are each month:" , list_bunnies)
    print("Here's a list of how many pairs of newborn bunnies there are each month:" , newborn)
    print("Here's a list of how many pairs of bunnies died each month:" , dead)
    print("Sadly, a total of" , total_dead , "pairs of bunnies died over the months.")