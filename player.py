from cmu_graphics import *
from settings import *
from main import *
from room import * 
class Player():
    def __init__(self):
        self.playerSpeed = 10
        self.directionX = 0
        self.directionY = 0
        self.obstaclePositions = None
    
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
        
    def step(self, obstaclePositions): #figure out how to make it so that the character doesnt move faster diagonally
        
        #Moves the map, while the player stays centered, giving the illusion of a camera. 
        possibleObstaclePositions = []
        for obstaclePosition in obstaclePositions:
            obstacleX, obstacleY = obstaclePosition
            possibleObstacleX = obstacleX - self.directionX * self.playerSpeed
            possibleObstacleY = obstacleY - self.directionY * self.playerSpeed
            possibleObstaclePosition = possibleObstacleX, possibleObstacleY
            possibleObstaclePositions.append(possibleObstaclePosition)

        if isColliding(app.playerPosition, possibleObstaclePositions) == False: #obstaclePositions not returned.
            if app.room.obstaclePositions != None:
                app.room.obstaclePositions = possibleObstaclePositions
            app.room.puzzleThreshold1 = app.room.puzzleThreshold1 - self.directionY * self.playerSpeed
            app.room.puzzleThreshold2 = app.room.puzzleThreshold2 - self.directionX * self.playerSpeed
        
        if app.room.puzzleThreshold1 >= app.playerPosition[1] or app.room.puzzleThreshold2 <= app.playerPosition[0]:
            app.mode = 'puzzle'
            
    def draw(self, playerImg):
        x,y = app.playerPosition
        drawImage(CMUImage(playerImg),x,y)

def isColliding(playerPosition, obstaclePositions):
    playerX, playerY = playerPosition

    for obstaclePosition in obstaclePositions:
        obstacleX, obstacleY = obstaclePosition
        
        if abs(obstacleX-playerX) < TILESIZE and abs(obstacleY-playerY) < TILESIZE:
            return True
    return False