width = 10
class AI:
    def __init__(self):
        self.currentlyDoing = "Forward"
    def turn(self):
        a = self.robot.position
        d = self.robot.rotation
      
        if self.robot.lookInFront() == "bot":
            self.robot.attack()
        else:
            self.towardsEnemy(self.robot.locateEnemy()[0])

    def towardsEnemy(self,enemyLocation):
        myLocation = self.robot.position
        
        delta=(enemyLocation[0]-myLocation[0],enemyLocation[1]-myLocation[1])
        if abs(delta[0]) > abs(delta[1]):
            if delta[0] < 0:
                targetOrientation =3
            else:
                targetOrientation = 1
        else:
            if delta[1]< 0:
                targetOrientation = 0
            else:
                targetOrientation = 2
        if self.robot.rotation == targetOrientation:
            if (delta[0]==2) or (delta[1]==2):
                self.robot.doBack()
            else:
                self.robot.goForth()
            '''
            if self.currentlyDoing == "Forward":
                self.robot.goForth()
                self.currentlyDoing = "Back"
            else:
                self.robot.goBack()
                self.currentlyDoing = "Forward"
            '''

        else:
            leftTurnsNeeded = (self.robot.rotation - targetOrientation) % 4
            if leftTurnsNeeded <= 2:
                self.robot.turnLeft()
            else:
                self.robot.turnRight()        