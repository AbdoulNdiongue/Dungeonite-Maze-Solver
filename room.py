from cmu_graphics import *
from main import *
from settings import *

class Room():
    def __init__(self, layout):
        self.layout = layout
    
    def roomSetup(self):
        self.relativeObstaclePos = set()

        #save the relative positions of the obstacles and player from each other
        for row_index, row in enumerate(self.layout):
            for col_index, val in enumerate(row):
            
                # setting x and y starting positions for each tile in the world map.
                x = col_index * TILESIZE 
                y = row_index * TILESIZE
                print(TILESIZE)

                if val == 'x':
                    self.relativeObstaclePos.add((x,y))
                elif val == 'p':
                    app.relativePlayerPos = (x,y)
                elif val == '1':
                    self.puzzleThreshold1 = y
                elif val == '2':
                    self.puzzleThreshold2 = x

        #using their positions relative to the player, shift the obstacles and puzzle thresholds
        self.obstaclePositions = set()
        self.differenceX = app.playerPosition[0] - app.relativePlayerPos[0]
        self.differenceY = app.playerPosition[1] - app.relativePlayerPos[1]
        self.puzzleThreshold1 = self.puzzleThreshold1 + self.differenceY 
        self.puzzleThreshold2 = self.puzzleThreshold2 + self.differenceX + TILESIZE

        for pos in self.relativeObstaclePos:
            x,y = pos
            actualX = x + self.differenceX
            actualY = y + self.differenceY

            self.obstaclePositions.add((actualX,actualY))

    def draw(self, obstacleImg):
        for obstaclePosition in self.obstaclePositions:
            x,y = obstaclePosition
            drawImage(CMUImage(obstacleImg),x,y)
        app.player.step(self.obstaclePositions)