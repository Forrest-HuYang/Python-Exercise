print("Please think of a number between 0 and 100!")
low=0
high=100
while True:
    guessAnswer=int((low + high)/2)
    print("Is your secret number "+ str(guessAnswer)+"?")
    indicator=input("Enter 'h' to indicate the guess is too high. \
           Enter 'l' to indicate the guess is too low. \
           Enter 'c' to indicate I guessed correctly.")
    if indicator == "h":
        high = guessAnswer
    elif indicator == "l":
        low = guessAnswer
    elif indicator == "c":
        break
    else :
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: " + str(guessAnswer))
        
    
