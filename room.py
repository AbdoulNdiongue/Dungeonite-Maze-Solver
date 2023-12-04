from cmu_graphics import *
from main import *
from settings import *
import random

class Room():
    def __init__(self, layout):
        self.layout = layout
    
    def roomSetup(self):
        self.relativeObstaclePos = set()

        if app.mode == 'puzzle1':
            visited = set()
            currCell = (1,1)
            self.createMaze(currCell, visited)

        #save the relative positions of the obstacles and player from each other
        #print(self.layout)
        for row_index, row in enumerate(self.layout):
            for col_index, val in enumerate(row):
            
                # setting x and y starting positions for each tile in the world map.
                
                x = col_index * TILESIZE 
                y = row_index * TILESIZE
                
                
                if val == 'x':
                    self.relativeObstaclePos.add((x,y))

                elif val == 'p':
                    app.relativePlayerPos = (x,y)

                elif val == '1':
                    if app.mode == 'spawn':
                        self.puzzleThreshold1 = y
                    elif app.mode == 'puzzle1':
                        self.puzzleThreshold1 = y
                        
                    elif app.mode == 'puzzle2':
                        self.puzzleThreshold1 = x
                        

                elif val == '2':
                    if app.mode == 'spawn':
                        self.puzzleThreshold2 = x

                    elif app.mode == 'puzzle1':
                        self.puzzleThreshold2 = x

                    elif app.mode == 'puzzle2':
                        self.puzzleThreshold2 = y

                elif val == 'k':
                    self.keyX = x
                    self.keyY = y
                    
                    

        #using their positions relative to the player, shift the obstacles and puzzle thresholds
        self.obstaclePositions = set()
        self.differenceX = app.playerPosition[0] - app.relativePlayerPos[0]
        self.differenceY = app.playerPosition[1] - app.relativePlayerPos[1]

        if app.mode == 'spawn':
            self.puzzleThreshold1 = self.puzzleThreshold1 + self.differenceY 
            self.puzzleThreshold2 = self.puzzleThreshold2 + self.differenceX 

        elif app.mode == 'puzzle1':
            self.puzzleThreshold1 = self.puzzleThreshold1 + self.differenceY 
            self.puzzleThreshold2 = self.puzzleThreshold2 + self.differenceX
            self.keyX = self.keyX + self.differenceX
            self.keyY = self.keyY + self.differenceY
            visited = set()
            currCell = (1,1)
            self.createMaze(currCell, visited)

        elif app.mode == 'puzzle2':
            self.puzzleThreshold1 = self.puzzleThreshold1 + self.differenceX  
            self.puzzleThreshold2 = self.puzzleThreshold2 + self.differenceY 
            self.keyX = self.keyX + self.differenceX
            self.keyY = self.keyY + self.differenceY

        for pos in self.relativeObstaclePos:
            x,y = pos
            actualX = x + self.differenceX
            actualY = y + self.differenceY

            self.obstaclePositions.add((actualX,actualY))

    def draw(self, obstacleImg):

        if app.mode == 'puzzle1' or app.mode == 'puzzle2':
            drawImage(CMUImage(app.keyImg),self.keyX,self.keyY)
            
        
        for obstaclePosition in self.obstaclePositions:
            x,y = obstaclePosition
            drawImage(CMUImage(obstacleImg),x,y)
        
        
    def drawMaze(self):
        pass
    
    def createMaze(self,currCell, visited):
        visited.add(currCell)

        nextCells = []
        nextCells.append((currCell[0] + 1, currCell[1]))
        nextCells.append((currCell[0], currCell[1] + 1))
        nextCells.append((currCell[0] - 1, currCell[1]))
        nextCells.append((currCell[0], currCell[1] - 1))

        print(nextCells)

        randomizedNextCells = []
        while len(nextCells) > 0:
            randomIndex = random.choice(range(len(nextCells)))
            randomizedNextCells.append(nextCells[randomIndex])
            nextCells.pop(randomIndex)

        #print(randomizedNextCells)

        for cell in randomizedNextCells:
            x,y = cell
            if cell in visited or x < 0 or y < 0 or self.layout[x][y] != ' ':
                pass
            
            else:
                #print(cell)
    
                self.layout[x][y] = 'x'
                maze = self.createMaze(cell, visited)
                #print(maze)
                if maze != None:
                    return maze
        return None