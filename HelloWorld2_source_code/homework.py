import easygui
class homework:                                          
    def __init__(self):                                
        self.done_level = 0                          
        self.done_string = "Untouched"                     
        self.handwriting = ""               
                
    def getDoneLevel(self, time, writing):
        if writing == "Good":
            self.done_level += time   
        elif writing == "OK":
            self.done_level += time * 2 
        elif writing == "Cursive Script":
            self.done_level = 0
            easygui.msgbox("You have finished your homework. Alas, your handwriting is so terrible that your teacher has ordered yo to do it again.")  
    
    def convertDoneString(self):
        if self.done_level > 20:                      
            self.done_string = "Overdone"            
        elif self.done_level > 10:                    
            self.done_string = "Well-done"           
        elif self.done_level > 5:                    
            self.done_string = "Unfinished"              
        else:                                          
            self.done_string = "Untouched"                 

    def do(self, time , writing):   
        self.getDoneLevel(time, writing)
        self.convertDoneString()
  
    def myhandwriting(self, handwriting):                 
        self.handwriting = handwriting

    def __str__(self):                                                                                                       
        msg = self.done_string + " homework with " + self.handwriting + " handwriting." 
        return msg             

class HomeworkView():
    def __init__(self, howework ):
        self.homework = homework

    def inputTime(self):
        return

    def displayHomeworkOnGUI(self):
        return

    def displayHomeworkOnCLI(self):
        return

def main( ) :       
    homework372 = homework()   
    homeworkView = HomeworkView(homework372)                                      
    time = int(easygui.enterbox("For how many hours will you do your homework?") )  
    writing = easygui.enterbox("How's your handwriting, Good, OK or Curive Script?")                                        
    easygui.msgbox ("doing damned homework for " + str(time) + " hours..." )     
    homework372.do(time,writing)                                                                                                                        
    homework372.myhandwriting(writing)                                                  
    print (homework372)                             
    easygui.msgbox(homework372)

main()
