# Import a library of functions called 'pygame'
import pygame
from math import pi
import easygui
# Define the colors we will use in RGB format
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300


class GraphicsEngine:

    #screen = None

    def initScreen(self):
        # Initialize the game engine
        pygame.init()

        # Set the height and width of the screen
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Example code for the draw module")
        self.screen.fill(WHITE)
        self.flip()

    def drawRect(self, color, top, left, width, height, line_width):
        # Draw a rectangle outline
        pygame.draw.rect(self.screen, color,
                         [top, left, width, height], line_width)

    def drawLine(self, color, start_pos_x, start_pos_y, end_pos_x, end_pos_y, line_width):
        # Draw a rectangle outline
        pygame.draw.line(self.screen, color, [start_pos_x, start_pos_y],
                         [end_pos_x, end_pos_y], line_width)

    def drawCircle(self, color, pos_x, pos_y, radius, line_width):
        # Draw a circle
        pygame.draw.circle(self.screen, color,
                           [pos_x, pos_y], radius, line_width)

    def flip(self):
        pygame.display.flip()

    def testDrawShapes(self):

        # All drawing code happens after the for loop and but
        # inside the main while done==False loop.
        screen = self.screen
        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw on the screen a GREEN line from (0,0) to (50.75)
        # 5 pixels wide.
        pygame.draw.line(screen, GREEN, [0, 0], [50, 30], 5)

        # Draw on the screen a GREEN line from (0,0) to (50.75)
        # 5 pixels wide.
        pygame.draw.lines(screen, BLACK, False, [
            [0, 80], [50, 90], [200, 80], [220, 30]], 5)

        # Draw on the screen a GREEN line from (0,0) to (50.75)
        # 5 pixels wide.
        pygame.draw.aaline(screen, GREEN, [0, 50], [50, 80], True)

        # Draw a rectangle outline
        pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
        # Draw a solid rectangle
        pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

        # Draw an ellipse outline, using a rectangle as the outside boundaries
        pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)

        # Draw an solid ellipse, using a rectangle as the outside boundaries
        pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])

        # This draws a triangle using the polygon command
        pygame.draw.polygon(
            screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

        # Draw an arc as part of an ellipse.
        # Use radians to determine what angle to draw.
        pygame.draw.arc(screen, BLACK, [210, 75, 150, 125], 0, pi/2, 2)
        pygame.draw.arc(screen, GREEN, [210, 75, 150, 125], pi/2, pi, 2)
        pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi, 3*pi/2, 2)
        pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)

        # Draw a circle
        pygame.draw.circle(screen, BLUE, [60, 250], 40)

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

    def waitToClose(self):
        # Loop until the user clicks the close button.
        done = False
        clock = pygame.time.Clock()

        while not done:
            # This limits the while loop to a max of 10 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(10)

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True

        # Be IDLE friendly
        pygame.quit()

class Initiator:
    
    

    def rect(color, top , left , width , height, line_width):
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
     

    def circle(center_x, center_y, radius, line_width ,color):
        ge = GraphicsEngine()
        ge.initScreen()
    # Draw a circle : color, center_x, center_y, radius, line_width
        ge.drawCircle(color, center_x, center_y, radius, line_width)
        ge.flip()
        ge.waitToClose()  
       


class Input_statistics:
    def __init__(self):

        self.initiator = Initiator()

    def original_input(self):
        choice = easygui.enterbox("If you want a line, please type 1; Rectangle, type 2; Circle, type 3.")
        result = self.shape_statistics(choice)
        return (result)
    

    def shape_statistics(self, choice):

        if choice == "1":
            a = int(easygui.enterbox("Enter length of line"))
            color = self.color_converter(easygui.enterbox("Enter colour of line, RED or BLUE?"))
            #self.initiator.line( color , 10 , 10 , 10 + a , 10 ,2 )
            return ([1 , color , 10 , 10, 10 + a , 10 ,2])

        if choice == "2":
            a = int(easygui.enterbox("Enter length of rectangle"))
            b = int(easygui.enterbox("Enter width of rectangle"))
            color = self.color_converter(easygui.enterbox("Enter colour of line, RED or BLUE?"))
            #self.initiator.rect( color , 150, 100 , a , b , 2 )
            return ([2 , color , 150 , 100, a , b ,2])

        if choice == "3":
            a = int(easygui.enterbox("Enter radius of circle"))
            color = self.color_converter(easygui.enterbox("Enter color of line, RED or BLUE?"))
            #self.initiator.circle( color , 60 , 200 , a , 2)
            return ([60 , 200, a ,2 ,color])

    def color_converter(self, color):
        if color == "RED": 
            return [255,0,0]
        if color == "BLUE":
            return [0,0,255]

i = 0
storage = []
num_shapes = int(input("How many shapes do you want to draw?"))
while i < num_shapes:
    a = Input_statistics()
    storage.append (a.original_input())
    i += 1

print (storage)

for i in range(len(storage)):
    if int((storage[i])[0]) == 1:
        del (storage[i])[0]
        Initiator.line((storage[i])[0] ,(storage[i])[1],(storage[i])[2],
                       (storage[i])[3],(storage[i])[4],(storage[i])[5])
    elif int((storage[i])[0]) == 2:
        del (storage[i])[0]
        Initiator.rect((storage[i])[0] ,(storage[i])[1],(storage[i])[2],
                       (storage[i])[3],(storage[i])[4],(storage[i])[5])
    else: 
        Initiator.circle((storage[i])[0] ,(storage[i])[1],(storage[i])[2],
                       (storage[i])[3],(storage[i])[4])


