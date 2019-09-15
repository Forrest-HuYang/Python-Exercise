class AI:
    def __init__(self):
        pass

    def turn(self):
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
        else:
            self.goTowards(self.robot.locateEnemy()[0],self.robot.locateEnemy()[1])

    def goTowards(self,enemyLocation,enemyrotation):
        self.robot.EnemyLocation = enemyLocation
        self.robot.EnemyRotation = enemyrotation
        self.robot.NextLocation = self.getNextLocation()
        self.delta = (self.robot.EnemyLocation[0]-self.robot.position[0],self.robot.EnemyLocation[1]-self.robot.position[1])
        self.newdelta = (self.robot.EnemyLocation[0] - self.robot.NextLocation[0] , self.robot.EnemyLocation[1] - self.robot.NextLocation[1])
        self.robot.EnemyTurnsNeeded = self.getEnemyTurnsNeeded()
        self.robot.targetOrientation = self.getTargetOrientation()
        self.robot.status = self.checkStatus()

        if self.robot.rotation == self.robot.targetOrientation and self.robot.status == 1:
            self.robot.goForth()

        elif self.robot.status == 3:
            if self.robot.EnemyTurnsNeeded != 0:
                self.robot.goForth()
            else:
                self.robot.doNothing()
        
        elif self.robot.status == 2:
            self.robot.Turns = self.getTurns()
            if self.robot.EnemyTurnsNeeded == 2:
                self.robot.goForth()
            else:
                self.robot.Turns.remove(self.robot.rotation)
                if ((self.robot.Turns[0] > self.robot.rotation) or (self.robot.Turns[0] == 0 and self.robot.rotation == 3))and not(self.robot.Turns[0] == 3 and self.robot.rotation == 0):
                    self.robot.turnRight()
                else:
                    self.robot.turnLeft()

        else:
            leftTurnsNeeded = (self.robot.rotation - self.robot.targetOrientation) % 4
            if leftTurnsNeeded <= 2:
                self.robot.turnLeft()
            else:
                self.robot.turnRight()
    

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

        nextlocation = [self.robot.position[0] + deltax,self.robot.position[1] + deltay]
        return nextlocation

    def getEnemyTurnsNeeded(self):
        if abs(self.newdelta[0]) > abs(self.newdelta[1]):
            if self.newdelta[0] < 0:
                newtargetOrientation = 1 
            else:
                newtargetOrientation = 3 
        else: 
            if self.newdelta[1] < 0:
                newtargetOrientation = 2 
            else:
                newtargetOrientation = 0
        enemyTurnsNeeded = abs(self.robot.EnemyRotation - newtargetOrientation)
        return enemyTurnsNeeded
  
    def getTurns(self):
        turn = []
        if self.delta[0] == 1 and self.delta[1] == 1:
            turn = [1,2]  
        elif self.delta[0] == 1 and self.delta[1] == -1:
            turn = [1,0]
        elif self.delta[0] == -1 and self.delta[1] == 1:
            turn = [3,2]
        elif self.delta[0] == -1 and self.delta[1] == -1:
            turn = [3,0]
        return turn

    def getTargetOrientation(self):
        if abs(self.delta[0]) > abs(self.delta[1]):
            if self.delta[0] < 0:
                targetOrientation = 3 #face left
            else:
                targetOrientation = 1 #face right
        else: 
            if self.delta[1] < 0:
                targetOrientation = 0 #faceup
            else:
                targetOrientation = 2 #face down
        return targetOrientation

    def checkStatus(self):
        step1 = abs(self.delta[0]) + abs(self.delta[1])
        step2 = abs(abs(self.delta[0]) - abs(self.delta[1]))

        if (step1 > 2):
            return 1
        elif (step1 == 2):
            if (step2 == 0):
                return 2
            elif (step2 == 2):
                return 3
        else:
            return 4
