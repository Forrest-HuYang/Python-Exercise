
numberOfVowels=0
for letter in s:
    if letter in [ 'a', 'e', 'i', 'o', 'u']:
        numberOfVowels += 1
print("Number of vowels: "+str(numberOfVowels))
