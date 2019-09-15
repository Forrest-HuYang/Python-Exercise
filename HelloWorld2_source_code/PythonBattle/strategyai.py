"""
AI Name: Random AI

Made by: Carter

Strategy:
Move around randomly.
Attack any robot in front of you.
"""

import random

class AI:
    def __init__(self):
        #Anything the AI needs to do before the game starts goes here.
        pass

    
    def turn(self):
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
            
        #else:
         #   self.goAnwdWait()

    def goAndWait(self):
        if self.robot.lookInFront() != "wall":
            self.robot.turnRight()

        if self.robot.lookInFront() == "bot":
            self.robot.attack()
