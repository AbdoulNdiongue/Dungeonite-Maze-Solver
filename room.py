from cmu_graphics import *
from main import *
from settings import *
import random
from PIL import Image

class Room():
    def __init__(self, layout):
        self.layout = layout
        self.showKey = True

    def roomSetup(self):
        self.relativeObstaclePos = set()

        if app.mode == 'puzzle1':
            visited = set()
            currCell = (11,9)
            end = (6,18)
            self.createMaze(currCell, visited, end)
            x = random.choice(range(1,11))
            y = random.choice(range(1,18))
            self.layout[x][y] = 'k'


        elif app.mode == 'puzzle2':
            visited = set()
            currCell = (1,6)
            end = (9,1)
            self.createMaze(currCell, visited, end)
            x = random.choice(range(1,11))
            y = random.choice(range(1,18))
            self.layout[x][y] = 'k'
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
                    #print(x/TILESIZE,y/TILESIZE)

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
        
        for obstaclePosition in self.obstaclePositions:
            x,y = obstaclePosition
            drawImage(CMUImage(obstacleImg),x,y)
    
    def createMaze(self,currCell, visited, end):
        visited.add(currCell)
        x1,y1 = currCell

        nextCells = []
        nextCells.append((x1 + 1, y1))
        nextCells.append((x1, y1 + 1))
        nextCells.append((x1 - 1, y1))
        nextCells.append((x1, y1 - 1))

        #print(f"next:{nextCells}")

        randomizedNextCells = []
        while len(nextCells) > 0:
            randomIndex = random.choice(range(len(nextCells)))
            randomizedNextCells.append(nextCells[randomIndex])
            nextCells.pop(randomIndex)

        #print(f"random:{randomizedNextCells}")

        for cell in randomizedNextCells:
            x,y = cell
            
            if cell in visited or x < 0 or y < 0  or x >= len(self.layout)-1 or y >= len(self.layout[0])-1 or self.layout[x][y] != ' ' or currCell == end:
                continue
            
            else:
                #print(currCell,cell)
                if x1-x != 0:
                    if y1+1 < len(self.layout[0])-2 and y1-1 > 0:
                        #print(x1,y1)
                        if (x1,y1+1) not in visited:
                            self.layout[x1][y1+1] = 'x'
                        if (x1,y1-1) not in visited:
                            self.layout[x1][y1-1] = 'x'
                        
                    
                elif y1-y != 0:
                    if x1+1 < len(self.layout)-2 and x1-1 > 0:
                        if (x1+1,y1) not in visited:
                            self.layout[x1+1][y1] = 'x'
                        if (x1-1,y1) not in visited:
                            self.layout[x1-1][y1] = 'x'
                        
                        
                
                
                maze = self.createMaze(cell, visited, end)
                #print(maze)
                if maze != None:
                    return maze
            
        #visited.remove(currCell)
            
        return None