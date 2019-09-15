"""
AI Name: Circle AI

Made by: Carter

Strategy: Drive in circles.  Attack any robot in your path.

"""

class RobotState(object):
    def __init__(self):
        pass

    def doAction(self,mystrategy):
        pass

class GoForth(RobotState):
    def doAction(self,mystrategy):
        mystrategy.robot.goForth()

class Context(object):
    def __init__(self):
        self.currState = GoForth()
    
    def setState(self,s):
        self.currState = s

    def doAction(self):
        self.currState.doAction(self)


class AI:
    def __init__(self):
        self.isFirstTurn = True
    def turn(self):
        strategy = Context()
        strategy.setState(GoForth())
        strategy.doAction()



        '''
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
        elif self.robot.lookInFront()== "wall":
            self.robot.turnLeft()
        else:
            self.robot.goForth()
        '''