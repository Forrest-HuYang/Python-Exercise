import random
secret = random.randint(1,99)
guess = 0
tries = 0
print "AHOY! i'm a pig. i have a secret!"
print "it is a number between 1 and 99. i'll give you 6 tries."
while guess != secret  and tries <6 :
    guess = input ("What's yer guess?" )
    if guess < secret:
        print "too low, you scurvy dog."
    elif guess > secret :
        print "too high ,pigs."

    tries = tries + 1

if guess == secret:
    print "Shit, you got it."
else:
    print "the secret number is ", secret

    


