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


class Initiator:

    def rect(color, top, left, width, height, line_width):
        ge = GraphicsEngine()
        ge.initScreen()
        ge.drawRect(color, top, left, width, height, line_width)
        ge.flip()
        ge.waitToClose()

    # draw a rect with parameter: color, start_x, start_y, end_x, end_y, line_width

    def line(color, start_x, start_y, end_x, end_y, line_width):
        ge = GraphicsEngine()
        ge.initScreen()
        ge.drawLine(color, start_x, start_y, end_x, end_y, line_width)
        ge.flip()
        ge.waitToClose()

    def circle(center_x, center_y, radius, line_width, color):
        ge = GraphicsEngine()
        ge.initScreen()
    # Draw a circle : color, center_x, center_y, radius, line_width
        ge.drawCircle(color, center_x, center_y, radius, line_width)
        ge.flip()
        ge.waitToClose()


class easygui:
    def enterbox(msg):
        return simpledialog.askstring("Input", msg,
                                      parent=GraphicsEngine.root)


class Input_statistics:
    def __init__(self):

        self.initiator = Initiator()

    def original_input(self):
        choice = easygui.enterbox(
            "If you want a line, please type 1; Rectangle, type 2; Circle, type 3.")
        result = self.shape_statistics(choice)
        return (result)

    def shape_statistics(self, choice):

        if choice == "1":
            a = int(easygui.enterbox("Enter length of line"))
            color = self.color_converter(easygui.enterbox(
                "Enter colour of line, RED or BLUE?"))
            # self.initiator.line( color , 10 , 10 , 10 + a , 10 ,2 )
            return ([1, color, 10, 10, 10 + a, 10, 2])

        if choice == "2":
            a = int(easygui.enterbox("Enter length of rectangle"))
            b = int(easygui.enterbox("Enter width of rectangle"))
            color = self.color_converter(easygui.enterbox(
                "Enter colour of line, RED or BLUE?"))
            # self.initiator.rect( color , 150, 100 , a , b , 2 )
            return ([2, color, 150, 100, a, b, 2])

        if choice == "3":
            a = int(easygui.enterbox("Enter radius of circle"))
            color = self.color_converter(easygui.enterbox(
                "Enter color of line, RED or BLUE?"))
            # self.initiator.circle( color , 60 , 200 , a , 2)
            return ([60, 200, a, 2, color])

    def color_converter(self, color):
        if color == "RED":
            return [255, 0, 0]
        if color == "BLUE":
            return [0, 0, 255]


#######################################

class Rectangle:

    def __init__(self, color, top, left, height, width):
        self.color = color
        self.top = top
        self.left = left
        self.height = height
        self.width = width
        self.line_width = 2

    def draw(self):
        Initiator.rect(self.color,  self.top, self.left, self.top +
                       self.height, self.left+self.width,  self.line_width)


def start():
    win = GraphicsEngine()
    # win.testDrawShapes()
    #a = int(easygui.enterbox("Enter radius of circle"))
    # GraphicsEngine.Run()


# start()
win = GraphicsEngine()

i = 0
storage = []
num_shapes = int(easygui.enterbox("How many shapes do you want to draw?"))
while i < num_shapes:
    a = Input_statistics()
    storage.append(a.original_input())
    i += 1

print(storage)


for i in range(len(storage)):
    if int((storage[i])[0]) == 1:
        del (storage[i])[0]
        Initiator.line((storage[i])[0], (storage[i])[1], (storage[i])[2],
                       (storage[i])[3], (storage[i])[4], (storage[i])[5])
    elif int((storage[i])[0]) == 2:
        del (storage[i])[0]
        Initiator.rect((storage[i])[0], (storage[i])[1], (storage[i])[2],
                       (storage[i])[3], (storage[i])[4], (storage[i])[5])
    else:
        Initiator.circle((storage[i])[0], (storage[i])[1], (storage[i])[2],
                         (storage[i])[3], (storage[i])[4])


#########
GraphicsEngine.Run()
