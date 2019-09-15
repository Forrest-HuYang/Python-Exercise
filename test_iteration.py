num = 10
for num in range(5):
    print(num)
print(num)

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)
    
school = 'Massachusetts Institute of Technology'

numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 
