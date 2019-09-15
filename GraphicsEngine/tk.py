# Import a library of functions called 'pygame'
from tkinter import Tk, Canvas, simpledialog
from math import pi
import time


class GraphicsEngine:
    root = None
    def __init__(self):

        if GraphicsEngine.root is None:
            GraphicsEngine.root = Tk()

        self.WIDTH, self.HEIGHT = (800, 600)
        # Initialize the game engine
        self.root = GraphicsEngine.root
        self.root.title("Graphics Engine")

       # Set the height and width of the screen

        self.root.geometry(str(self.WIDTH) + "x" +
                           str(self.HEIGHT))  # Set Window Size
        self.root.resizable(False, False)  # Not Resizable

        # Setup the window canvas
        self.canvas = Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
        self.canvas.pack()

        self.old_coords = None
        self.doubleClicked = False

    def Run():
        GraphicsEngine.root.mainloop()

    def drawRect(self, color, top, left, width, height, line_width):
        # Draw a rectangle outline
        # self.canvas.create_rectangle(self.x - self.width/2, self.y - self.height/2, self.x + self.width/2,
        #                             self.y + self.height/2, outline=self.lineColour, fill=self.fillColour, width=self.lineThickness)
        self.canvas.create_rectangle(
            top, left, top+height, left+width, outline=color, width=line_width)

    def drawLine(self, color, start_pos_x, start_pos_y, end_pos_x, end_pos_y, line_width):
        # Draw a Line outline
        self.canvas.create_line(start_pos_x, start_pos_y, end_pos_x,
                                end_pos_y, fill=color, width=line_width)

    def drawCircle(self, color, pos_x, pos_y, radius, line_width):
        # Draw a circle
        # self.controller.canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius,
        #		                                   self.y + self.radius, outline=self.lineColour, fill=self.fillColour, width=self.lineThickness)
        self.canvas.create_oval(pos_x-radius, pos_y-radius, pos_x+radius,
                                pos_y+radius, outline=color, width=line_width)

    def drawing(self, event):
        x, y = event.x, event.y
        if self.old_coords:
            x1, y1 = self.old_coords
            self.canvas.create_line(x, y, x1, y1)
        self.old_coords = x, y

    def update(self):
        pass

    def onMouseMove(self, event):

        x, y = event.x, event.y
        if self.old_coords:
            x1, y1 = self.old_coords
            self.canvas.delete("track_line")
            self.canvas.create_line(x, y, x1, y1, tag='track_line')
        # self.old_coords = x, y

    def onMouseDown(self, event):
        x, y = event.x, event.y
        # if self.old_coords:
        #    x1, y1 = self.old_coords
        # self.canvas.create_line(x, y, x1, y1)
        self.old_coords = x, y

    def onMouseDoubleClick(self, event):
        # self.onMouseUp(event)
        # self.old_coords = None
        self.doubleClicked = True

    def onMouseUp(self, event):
        x, y = event.x, event.y
        if self.old_coords:
            x1, y1 = self.old_coords
            self.canvas.delete('track_line')
            self.canvas.create_line(x, y, x1, y1)

        self.old_coords = (x, y) if not self.doubleClicked else None
        self.doubleClicked = False

    def testDrawShapes(self):

        # Draw on the screen a GREEN line from (0,0) to (50.75)
        # 5 pixels wide.
        self.drawLine('green', 300, 300, 350, 350, 2)

        # Draw a rectangle outline
        self.drawRect('red', 50, 50, 150, 150, 2)
        # Draw a solid rectangle

        # Draw a circle
        self.drawCircle('blue', 200, 200, 50, 2)

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        self.update()

        # enable to draw a line following the mouse move
        self.canvas.bind('<Motion>', self.onMouseMove)
        # self.canvas.bind('<Button-1>', self.onMouseDown)
        self.canvas.bind('<ButtonRelease-1>', self.onMouseUp)
        self.canvas.bind('<Double-Button-1>', self.onMouseDoubleClick)

    def drawText(self, color, start_x, start_y, myText):
        self.canvas.create_text(start_x, start_y, text=myText, fill=color, font="Times 20 italic bold", anchor="nw")

class easygui:
    def enterbox(msg):
        return simpledialog.askstring("Input", msg,
                                      parent=GraphicsEngine.root)


class Input_statistics:

    def original_input(self):
        choice = easygui.enterbox(
            "If you want a line, please type 1; Rectangle, type 2; Circle, type 3.")
        result = self.shape_statistics(choice)
        return (result)

    def shape_statistics(self, choice):

        if choice == "1":
            a = int(easygui.enterbox("Enter length of line"))
            color = easygui.enterbox("Enter colour of line, RED or BLUE?")
            myLine = Line( color, 150, 10, 150 + a, 10)
            return myLine

        if choice == "2":
            a = int(easygui.enterbox("Enter length of rectangle"))
            b = int(easygui.enterbox("Enter width of rectangle"))
            color = easygui.enterbox("Enter colour of line, RED or BLUE?")
            myRect = Rectangle(color, 150, 100, a, b)
            return myRect

        if choice == "3":
            a = int(easygui.enterbox("Enter radius of circle"))
            color = easygui.enterbox("Enter color of line, RED or BLUE?")
            myCircle = Circle(color, 200, 200, a)
            return myCircle



######################################
        
class Line:

    def __init__(self, color, start_x, start_y, end_x, end_y):
        self.color = color
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.line_width = 2

    def getArea(self):
        return (0)

    def getCircum(self):
        return 0

    def draw(self, ge):
        ge.drawLine(self.color,  self.start_x, self.start_y, self.end_x, self.end_y,  self.line_width)
    
    def drawShapeInfo(self, ge):
        text = "Area = " + str(self.getArea())  + "   Circum = " +  str(self.getCircum())
        ge.drawText(self.color, self.start_x , self.start_y, text)

class Rectangle:

    def __init__(self, color, top, left, height, width):
        self.color = color
        self.top = top
        self.left = left
        self.height = height
        self.width = width
        self.line_width = 2

    def getArea(self):
        area = self.height * self.width
        return (area)

    def getCircum(self):
        circum = (self.height + self.width) * 2
        return circum

    def draw(self, ge):
        ge.drawRect(self.color,  self.top, self.left, self.top +
                       self.height, self.left+self.width,  self.line_width)
    
    def drawShapeInfo(self, ge):
        text = "Area = " + str(self.getArea())  + "   Circum = " +  str(self.getCircum())
        ge.drawText(self.color, self.top , self.left , text)

class Circle:

    def __init__(self, color , center_x , center_y, radius):
        self.color = color
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.line_width = 2

    def getArea(self):
        area = self.radius * (3.14)**2
        return (area)

    def getCircum(self):
        circum = self.radius * 2 * 3.14
        return circum

    def draw(self,ge):
        ge.drawCircle(self.color,  self.center_x, self.center_y, self.radius,  self.line_width)
    
    def drawShapeInfo(self, ge):
        text = "Area = " + str(self.getArea())  + "   Circum = " +  str(self.getCircum())
        ge.drawText(self.color,self.center_x, self.center_y , text)



def start():
    win = GraphicsEngine()
    # win.testDrawShapes()
    # a = int(easygui.enterbox("Enter radius of circle"))
    # GraphicsEngine.Run()


# start()
mainWindow = GraphicsEngine()

i = 0
storage = []
num_shapes = int(easygui.enterbox("How many shapes would you want to draw?"))
while i < num_shapes:
    input_win = Input_statistics()
    a = input_win.original_input()
    storage.append(a)
    i += 1

print(storage)


for i in range(len(storage)):
    storage[i].draw(mainWindow)
    storage[i].drawShapeInfo(mainWindow)


    


#########
GraphicsEngine.Run()
