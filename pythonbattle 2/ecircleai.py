# Listing 26-1
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# PythonBattle AI - first attempt to beat CircleAI

# Note that this is not a complete Python program itself,
#   it is a module called by the PythonBattle program.
# Save this as something like "betterthancircleai.py"
#   and try it in a battle against circleai.
width = 10


class AI:
    def __init__(self):
        self.currentlyDoing = "Forward"

    def IsAtCorner(self):
        a = self.robot.position
        d = self.robot.rotation
        return ((a == (2, 2) and d == 3)or (a == (2, 9) and d == 2) or (a == (9, 9) and d == 1) or (a == (9, 2) and d == 0))

    def turn(self):
        a = self.robot.position
        d = self.robot.rotation
        # print(str(self.robot.position))
        # print(d)
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
            self.currentlyDoing = "turn left"
        elif (a == (2, 5) or a == (9, 5)) and self.currentlyDoing != "forward":
            self.robot.turnRight()
            self.currentlyDoing = "forward"
        elif self.currentlyDoing == "turn left":
            self.robot.turnLeft()
            self.currentlyDoing = "forward"
        elif self.IsAtCorner():
            self.robot.doNothing()
            self.currentlyDoing = "wait"
        else:
            self.robot.goForth()
