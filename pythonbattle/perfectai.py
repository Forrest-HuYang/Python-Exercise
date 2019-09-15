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
        delta = (self.robot.EnemyLocation[0]-self.robot.position[0],self.robot.EnemyLocation[1]-self.robot.position[1])
    

 
        if self.robot.rotation == 0:
            deltax = 0
            deltay = -1 

        if self.robot.rotation == 1:
            deltax = 1
            deltay = 0 
        
        if self.robot.rotation == 2:
            deltax = 0
            deltay = 1 
        
        if self.robot.rotation == 3:
            deltax = -1
            deltay = 0

        self.robot.nextlocation = [self.robot.position[0] + deltax,self.robot.position[1] + deltay]
        newdelta = (self.robot.EnemyLocation[0]-self.robot.nextlocation[0],self.robot.EnemyLocation[1]-self.robot.nextlocation[1])

        if abs(newdelta[0]) > abs(newdelta[1]):
            if delta[0] < 0:
                newtargetOrientation = 1 #face left
            else:
                newtargetOrientation = 3 #face right
        else: 
            if delta[1] < 0:
                newtargetOrientation = 2 #faceup
            else:
                newtargetOrientation = 0

        if delta[0] == 1 and delta[1] == 1:
            turn = [1,2]  
        if delta[0] == 1 and delta[1] == -1:
            turn = [1,0]
        if delta[0] == -1 and delta[1] == 1:
            turn = [3,2]
        if delta[0] == 1 and delta[1] == 1:
            turn = [3,0]

        enemyTurnsNeeded = abs(self.robot.EnemyRotation - newtargetOrientation)
        print (enemyTurnsNeeded)
        print("my ", str(self.robot.position))
        print("enemy ",str(self.robot.EnemyLocation))
        print(self.robot.EnemyRotation)
        print(self.robot.nextlocation)
        print(enemyTurnsNeeded == 2)


        if abs(delta[0]) > abs(delta[1]):
            if delta[0] < 0:
                targetOrientation = 3 #face left
            else:
                targetOrientation = 1 #face right
        else: 
            if delta[1] < 0:
                targetOrientation = 0 #faceup
            else:
                targetOrientation = 2 #face down

        
        if self.robot.rotation == targetOrientation and (abs(delta[0]) + abs(delta[1])) > 2:
            self.robot.goForth()
        elif abs(abs(delta[0]) - abs(delta[1])) == 2 and (abs(delta[0]) + abs(delta[1])) == 2:
            if abs(self.robot.EnemyRotation - self.robot.rotation) != 2:
                self.robot.goForth()
            else:
                self.robot.doNothing()
        
        elif abs(abs(delta[0]) - abs(delta[1])) == 0 and (abs(delta[0]) + abs(delta[1])) == 2:
            if enemyTurnsNeeded == 2:
                self.robot.goForth()
            else:
                turn.remove(self.robot.rotation)
                if turn[0] > self.robot.rotation or (turn[0] == 0 and self.robot.rotation == 3):
                    self.robot.turnRight()
                else:
                    self.robot.turnLeft()
                    

        else:
            leftTurnsNeeded = (self.robot.rotation - targetOrientation) % 4
            if leftTurnsNeeded <= 2:
                self.robot.turnLeft()
            else:
                self.robot.turnRight()
