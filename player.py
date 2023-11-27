from cmu_graphics import *
from settings import *

class Player():
    def __init__(self, playerPosition):
        self.playerPosition = playerPosition
        self.playerSpeed = 10
        self.directionX = 0
        self.directionY = 0
    
    def move(self,direction):
        if direction == 'right':
            self.directionX = 1
        elif direction == 'left':
            self.directionX = -1
        elif direction == 'up':
            self.directionY = -1
        elif direction == 'down':
            self.directionY = 1
        
    
    def stopMove(self,direction):
        if direction == 'right' and self.directionX != -1:
            self.directionX = 0
        elif direction == 'left' and self.directionX != 1:
            self.directionX = 0

        if direction == 'up' and self.directionY != 1:
            self.directionY = 0
        elif direction == 'down' and self.directionY != -1:
            self.directionY = 0
        
    
        
    def draw(self, playerImg):
        x,y = self.playerPosition
        drawImage(CMUImage(playerImg),x,y)

def isColliding(playerPosition, obstaclePositions):
    playerX, playerY = playerPosition

    for obstaclePosition in obstaclePositions:
        obstacleX, obstacleY = obstaclePosition
        
        if abs(obstacleX-playerX) < TILESIZE and abs(obstacleY-playerY) < TILESIZE:
            return True
    return False