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
        self.robot.Turns = self.getTurns()
        self.robot.targetOrientation = self.getTargetOrientation()

        print ("turns needed ", str(self.robot.EnemyTurnsNeeded))
        print("my ", str(self.robot.position))
        print("enemy ",str(self.robot.EnemyLocation))
        print(self.robot.EnemyRotation)
        print("newdeltais" , str(self.newdelta))

        if self.robot.rotation == self.robot.targetOrientation and (abs(self.delta[0]) + abs(self.delta[1])) > 2:
            self.robot.goForth()

        elif abs(abs(self.delta[0]) - abs(self.delta[1])) == 2 and (abs(self.delta[0]) + abs(self.delta[1])) == 2:
            if abs(self.robot.EnemyRotation - self.robot.rotation) != 2:
                self.robot.goForth()
            else:
                self.robot.doNothing()
        
        elif abs(abs(self.delta[0]) - abs(self.delta[1]) == 0) and (abs(self.delta[0]) + abs(self.delta[1])) == 2:
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
        print("shit", str(newtargetOrientation))
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
