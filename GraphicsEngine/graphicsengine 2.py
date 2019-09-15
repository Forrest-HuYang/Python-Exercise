# Import a library of functions called 'pygame'
import pygame
from math import pi
# Define the colors we will use in RGB format
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300


class GraphicsEngine:

    screen = None

    def initScreen(self):
        # Initialize the game engine
        pygame.init()

        # Set the height and width of the screen
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Example code for the draw module")
        self.screen.fill(WHITE)

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


def start():

    # Create an GraphicsEngine Object to enable draw shape on screen
    ge = GraphicsEngine()

    # At first, initialize to screen, size is 400x300
    ge.initScreen()
    # ge.testDrawShapes()

    # draw a rect with parameter: color, top, left, width, height, line_width
    ge.drawRect(RED, 150, 100, 50, 20, 2)

    # draw a rect with parameter: color, start_x, start_y, end_x, end_y, line_width
    ge.drawLine(RED, 10, 10, 150, 130, 2)

    # Draw a circle : color, center_x, center_y, radius, line_width
    ge.drawCircle(BLUE, 60, 250, 40, 2)

    # Show the image really.
    ge.flip()

    # waiting the keyboard or mouse to close the window and return.
    ge.waitToClose()
    print("Exited.........")


start()
