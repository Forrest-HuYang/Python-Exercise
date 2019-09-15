alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
new_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
key = int(input("what is the key?"))
msg = input("what is the message?")
for i in range(26 - key):
    new_alphabet[i] = alphabet[i + 5]
for k in range(26 - key , 26):
    y = k + key -26
    new_alphabet[k] = alphabet[y]
alphabet_order = []
pos = 0
for word in msg:
    for i in range (26):
        if alphabet[i] == word:
            word_num = i
            alphabet_order.append(i)

list_msg = tuple(msg)
for w in list_msg:
    list_msg[i] = new_alphabet[int(alphabet_order[i])]
print(alphabet_order)
print (new_alphabet)
print (msg)
