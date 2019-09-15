import easygui
class teacher:
    def check(self , answer):
        if answer == "Kun":
            easygui.msgbox("19372, i have received your homework. You are now free to go.")
            return "done"
        else:
            easygui.msgbox("do it again, pig!")
            return "far from done"

class student:
    def homework(self):
        answer = easygui.enterbox("What is the chemical symbol for Shit?")
        return answer

me = student()
myhomework = me.homework()
print (myhomework)

Kun = teacher()
returned_homework = Kun.check(myhomework)
print ("My homework is" , returned_homework)
