class AI:
    def __init__(self):
        pass
    def turn(self):
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
        else:
            self.goTowards(self.robot.locateEnemy()[0])
    def goTowards(self,enemyLocation):
        myLocation = self.robot.position
        self.robot.EnemyRotation = self.robot.locateEnemy()[1]
        delta = (enemyLocation[0]-myLocation[0],enemyLocation[1]-myLocation[1])

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
        elif self.robot.rotation == targetOrientation and (abs(delta[0]) + abs(delta[1])) = 2:
            if 
            self.robot.doNothing()
        else:
            leftTurnsNeeded = (self.robot.rotation - targetOrientation) % 4
            if leftTurnsNeeded <= 2:
                self.robot.turnLeft()
            else:
                self.robot.turnRight()
