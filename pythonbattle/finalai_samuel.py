

from enum import Enum


class AIStepDelta(Enum):
    FARAWAY = 3
    CRITICALITY_DIAG = 2
    CRITICALITY_LINE = 1
    ADJACENCY = 0


class AIRotation(Enum):
    LEFT = 1
    RIGHT = 2


class AI:

    def __init__(self):
        pass

    def turn(self):
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
        else:
            self.goTowards(self.robot.locateEnemy()[
                           0], self.robot.locateEnemy()[1])

    def goTowards(self, enemyLocation, enemyrotation):
        self.robot.enemyLocation = enemyLocation
        self.robot.enemyRotation = enemyrotation
        self.robot.nextLocation = self.getNextLocation()
        self.delta = (self.robot.enemyLocation[0]-self.robot.position[0],
                      self.robot.enemyLocation[1]-self.robot.position[1])
        self.newDelta = (self.robot.enemyLocation[0] - self.robot.nextLocation[0],
                         self.robot.enemyLocation[1] - self.robot.nextLocation[1])
        self.robot.enemyTurnsNeeded = self.getEnemyTurnsNeeded()
        self.robot.turns = self.getTurns()
        self.robot.targetOrientation = self.getTargetOrientation()

        print("turns needed: ", str(self.robot.enemyTurnsNeeded))
        print("my position: ", str(self.robot.position))
        print("enemy ", str(self.robot.enemyLocation))
        print('enemy rotation:', self.robot.enemyRotation)
        print("newDelta is ", str(self.newDelta))

        if self.robot.rotation == self.robot.targetOrientation and self.checkStepDelta() == AIStepDelta.FARAWAY:
            self.robot.goForth()

        elif self.checkStepDelta() == AIStepDelta.CRITICALITY_DIAG or self.checkStepDelta() == AIStepDelta.CRITICALITY_LINE:
            if abs(self.robot.enemyRotation - self.robot.rotation) != 2 or self.robot.enemyTurnsNeeded == 2:
                self.robot.goForth()
            else:
                if self.robot.enemyTurnsNeeded != 2:
                    self.robot.turns.remove(self.robot.rotation)
                    if (self.selectRotation() == AIRotation.RIGHT):
                        self.robot.turnRight()
                    else:
                        self.robot.turnLeft()
                else:
                    self.robot.doNothing()
        else:
            leftTurnsNeeded = (self.robot.rotation -
                               self.robot.targetOrientation) % 4
            if leftTurnsNeeded <= 2:
                self.robot.turnLeft()
            else:
                self.robot.turnRight()

    def selectRotation(self):
        if ((self.robot.turns[0] > self.robot.rotation) or (self.robot.turns[0] == 0 and self.robot.rotation == 3)) \
                and not(self.robot.turns[0] == 3 and self.robot.rotation == 0):
            return AIRotation.RIGHT
        else:
            return AIRotation.LEFT

    def checkTurnDelta(self):
        pass

    def checkStepDelta(self):
        step1 = abs(self.delta[0]) + abs(self.delta[1])
        step2 = abs(abs(self.delta[0]) - abs(self.delta[1]))

        if (step1 > 2):
            return AIStepDelta.FARAWAY
        elif (step1 == 2):
            if (step2 == 0):
                return AIStepDelta.CRITICALITY_DIAG
            elif (step2 == 2):
                return AIStepDelta.CRITICALITY_LINE
        else:
            return AIStepDelta.ADJACENCY

    def getNextLocation(self):
        if self.robot.rotation == 0:
            deltax = 0
            deltay = -1

        elif self.robot.rotation == 1:
            deltax = 1
            deltay = 0

        elif self.robot.rotation == 2:
            deltax = 0
            deltay = 1

        elif self.robot.rotation == 3:
            deltax = -1
            deltay = 0

        nextlocation = [self.robot.position[0] +
                        deltax, self.robot.position[1] + deltay]
        return nextlocation

    def getEnemyTurnsNeeded(self):
        if abs(self.newDelta[0]) > abs(self.newDelta[1]):
            if self.newDelta[0] < 0:
                newtargetOrientation = 1
            else:
                newtargetOrientation = 3
        else:
            if self.newDelta[1] < 0:
                newtargetOrientation = 2
            else:
                newtargetOrientation = 0
        print("shit", str(newtargetOrientation))
        enemyTurnsNeeded = abs(self.robot.enemyRotation - newtargetOrientation)
        return enemyTurnsNeeded

    def getTurns(self):
        turn = []
        if self.delta[0] == 1 and self.delta[1] == 1:
            turn = [1, 2]
        elif self.delta[0] == 1 and self.delta[1] == -1:
            turn = [1, 0]
        elif self.delta[0] == -1 and self.delta[1] == 1:
            turn = [3, 2]
        elif self.delta[0] == -1 and self.delta[1] == -1:
            turn = [3, 0]
        return turn

    def getTargetOrientation(self):
        if abs(self.delta[0]) > abs(self.delta[1]):
            if self.delta[0] < 0:
                targetOrientation = 3  # face left
            else:
                targetOrientation = 1  # face right
        else:
            if self.delta[1] < 0:
                targetOrientation = 0  # faceup
            else:
                targetOrientation = 2  # face down
        return targetOrientation
