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
        
        #changing animation
        if self.directionX == 1:
            for frame in range(4):
                app.playerImg = Image.open(f"graphics/player/right/right_{frame}.png")

        elif self.directionX == -1:
            for frame in range(4):
                app.playerImg = Image.open(f"graphics/player/left/left_{frame}.png")

        elif self.directionY == -1:
            for frame in range(4):
                app.playerImg = Image.open(f"graphics/player/up/up_{frame}.png")

        elif self.directionY == 1:
            for frame in range(4):
                app.playerImg = Image.open(f"graphics/player/down/down_{frame}.png")
            
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

            #Room Movement
            #print(app.room.puzzleThreshold1,  app.room.puzzleThreshold2)
            
            if app.mode == 'spawn':

                app.room.puzzleThreshold1 = app.room.puzzleThreshold1 - self.directionY * self.playerSpeed
                app.room.puzzleThreshold2 = app.room.puzzleThreshold2 - self.directionX * self.playerSpeed
                if abs(app.room.puzzleThreshold1 - app.playerPosition[1]) < self.playerSpeed :
                    app.room = Room(PUZZLE_ONE)
                    app.mode = 'puzzle1'
                    app.room.roomSetup()
                    

                elif abs(app.room.puzzleThreshold2 - app.playerPosition[0]) < self.playerSpeed:
                    app.room = Room(PUZZLE_TWO)
                    app.mode = 'puzzle2'
                    app.room.roomSetup()
                    
                    
                    
            if app.mode == 'puzzle1':
                #print(app.room.keyX, app.room.keyY)
                app.room.puzzleThreshold1 = app.room.puzzleThreshold1 - self.directionY * self.playerSpeed
                app.room.puzzleThreshold2 = app.room.puzzleThreshold2 - self.directionX * self.playerSpeed
                app.room.keyX = app.room.keyX - self.directionX * self.playerSpeed
                app.room.keyY = app.room.keyY - self.directionY * self.playerSpeed

                if abs(app.room.keyX - app.playerPosition[0]) <= self.playerSpeed and abs(app.room.keyY - app.playerPosition[1]) <= self.playerSpeed:
                    app.keys.add('key1')
                    app.room.showKey == False

                if abs(app.room.puzzleThreshold1 - app.playerPosition[1]) < self.playerSpeed:
                    app.room = Room(SPAWN_ROOM)
                    app.room.layout[8][10] = ' '
                    app.room.layout[8][18] = ' '
                    app.room.layout[1][10] = 'p'
                    app.mode = 'spawn'
                    app.room.roomSetup()

                elif abs(app.room.puzzleThreshold2 - app.playerPosition[0]) < self.playerSpeed and app.keys == {'key1','key2'}:
                    app.room = Room(END_ROOM)
                    app.mode = 'end'
                    app.room.roomSetup()
                
                

            if app.mode == 'puzzle2':

                app.room.puzzleThreshold1 = app.room.puzzleThreshold1 - self.directionX * self.playerSpeed
                app.room.puzzleThreshold2 = app.room.puzzleThreshold2 - self.directionY * self.playerSpeed
                app.room.keyX = app.room.keyX - self.directionX * self.playerSpeed
                app.room.keyY = app.room.keyY - self.directionY * self.playerSpeed

                if abs(app.room.keyX - app.playerPosition[0]) <= self.playerSpeed and abs(app.room.keyY - app.playerPosition[1]) <= self.playerSpeed:
                    app.keys.add('key2')
                    app.room.showKey == False

                if abs(app.room.puzzleThreshold1 - app.playerPosition[0]) < self.playerSpeed:
                    app.room = Room(SPAWN_ROOM)
                    app.room.layout[8][18] = 'p'
                    app.mode = 'spawn'
                    app.room.roomSetup()

                elif abs(app.room.puzzleThreshold2 - app.playerPosition[1]) < self.playerSpeed and app.keys == {'key1','key2'}:
                    app.room = Room(END_ROOM)
                    app.mode = 'end'
                    app.room.roomSetup()
                
                
            
    def draw(self, playerImg):
        if app.mode == 'puzzle1' or app.mode == 'puzzle2':
            if app.room.showKey:
                drawImage(CMUImage(app.keyImg),app.room.keyX,app.room.keyY)

        x,y = app.playerPosition
        drawImage(CMUImage(playerImg),x,y)

        

        if len(app.keys) > 0:
            drawImage(CMUImage(app.keyImg),100,100)
            drawLabel(f'x{len(app.keys)}', 175,120, size = 40, fill = 'white')

def isColliding(playerPosition, obstaclePositions):
    playerX, playerY = playerPosition

    for obstaclePosition in obstaclePositions:
        obstacleX, obstacleY = obstaclePosition
        
        if abs(obstacleX-playerX) < TILESIZE*90/100 and abs(obstacleY-playerY) < TILESIZE*90/100:
            return True
    return False