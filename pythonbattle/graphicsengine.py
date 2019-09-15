from tkinter import Tk, Canvas, PhotoImage
from math import pi
import time
from PIL import Image, ImageTk


class GraphicsEngine:
    root = None

    def __init__(self, width, height):

        if GraphicsEngine.root is None:
            GraphicsEngine.root = Tk()

        self.WIDTH, self.HEIGHT = (width, height)
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

    def Run(self):
        GraphicsEngine.root.mainloop()

    def _from_rgb(self, rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb

    def drawRect(self, color, top, left, width, height, line_width=0):
        # Draw a rectangle outline
        # self.canvas.create_rectangle(self.x - self.width/2, self.y - self.height/2, self.x + self.width/2,
        #                             self.y + self.height/2, outline=self.lineColour, fill=self.fillColour, width=self.lineThickness)
        if (line_width == 0):
            self.canvas.create_rectangle(
                top, left, top+height, left+width, outline=color, fill=color)
        else:
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

    def drawText(self, fg_color, start_x, start_y, text, font_size=20):
        self.canvas.create_text(
            start_x, start_y, fill=fg_color, font=("Times italic bold", font_size), text=text, anchor='nw')

    def drawImage(self, imgTk, start_x, start_y):
        self.canvas.create_image(start_x, start_y, anchor='nw', image=imgTk)

    def drawing(self, event):
        x, y = event.x, event.y
        if self.old_coords:
            x1, y1 = self.old_coords
            self.canvas.create_line(x, y, x1, y1)
        self.old_coords = x, y

    def update(self):
        self.canvas.pack()
        #self.canvas.pack(fill='both', expand=1)
        self.canvas.update()

    def onMouseMove(self, event):

        x, y = event.x, event.y
        if self.old_coords:
            x1, y1 = self.old_coords
            self.canvas.delete("track_line")
            self.canvas.create_line(x, y, x1, y1, tag='track_line')
        #self.old_coords = x, y

    def onMouseDown(self, event):
        x, y = event.x, event.y
        # if self.old_coords:
        #    x1, y1 = self.old_coords
        # self.canvas.create_line(x, y, x1, y1)
        self.old_coords = x, y

    def onMouseDoubleClick(self, event):
        # self.onMouseUp(event)
        #self.old_coords = None
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

        image = Image.open("element-slicling.jpg")  # ("DozerRed.png")
        self.imgTk = ImageTk.PhotoImage(image.rotate(90))
        self.drawImage(self.imgTk, 0, 0)

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        self.update()

        # enable to draw a line following the mouse move
        #self.canvas.bind('<Motion>', self.onMouseMove)
        #self.canvas.bind('<Button-1>', self.onMouseDown)
        #self.canvas.bind('<ButtonRelease-1>', self.onMouseUp)
        #self.canvas.bind('<Double-Button-1>', self.onMouseDoubleClick)


def start():
    #root = Tk()
    win = GraphicsEngine(800, 600)
    win.testDrawShapes()
    win.Run()


'''
If this was the file that was set to run then launch the application. Else do nothing.
The application can only run if this was the file set to run. 'py main.py'
'''
if __name__ == '__main__':
    start()
