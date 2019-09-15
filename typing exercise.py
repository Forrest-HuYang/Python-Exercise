print("asdfghjkl")
typing = "asdfghjkl"
answer=str(input("please type the words above: "))

for i in range(len(typing)):
    print(i+1, typing[i])
    if i >= len(answer) :
        break
    elif answer[i]==typing[i]:
            print("letter",  i+1,  " is correct")
    else:
            print("letter", i+1 , "is incorrect")
    
if typing==answer:
     print("good job")
else:
     print("You are a 猪 pig 돼지 свинья الخنازير Schweine หม ูEl cerdo γουρούνι ")
