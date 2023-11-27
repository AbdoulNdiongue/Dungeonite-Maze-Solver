from cmu_graphics import *
from settings import *
from player import *
from obstacles import *
from PIL import Image

def onAppStart(app):
    app.map = WORLD_MAP

    # Create the Images
    app.playerImg = Image.new('RGB', (TILESIZE, TILESIZE), (0,255,255))
    app.obstacleImg = Image.new('RGB', (TILESIZE, TILESIZE), (255,0,255))

    #Find positions to draw the player and obstacles
    app.playerPosition = ((WIDTH//TILESIZE)*TILESIZE/2, (HEIGHT//TILESIZE)*TILESIZE/2) #places player in the middle of the screen 
    app.relativeObstaclePos = set()

    #save the relative positions of the obstacles and player from each other
    for row_index, row in enumerate(WORLD_MAP):
        for col_index, val in enumerate(row):
        
            # setting x and y starting positions for each tile in the world map.
            x = col_index * TILESIZE 
            y = row_index * TILESIZE

            if val == 'x':
                app.relativeObstaclePos.add((x,y))
            if val == 'p':
                app.relativePlayerPos = (x,y)

    #using their positions relative to the player, shift the obstacles
    app.obstaclePositions = set()
    app.differenceX = app.playerPosition[0] - app.relativePlayerPos[0]
    app.differenceY = app.playerPosition[1] - app.relativePlayerPos[1]
    
    for pos in app.relativeObstaclePos:
        x,y = pos
        actualX = x + app.differenceX
        actualY = y + app.differenceY

        app.obstaclePositions.add((actualX,actualY))

    #Player
    app.player = Player(app.playerPosition)

def onKeyPress(app,key):
    app.player.move(key)
    
def onKeyRelease(app,key):
    app.player.stopMove(key)

def onStep(app):

    app.player.step(app.obstaclePositions)
    
def redrawAll(app):
    app.player.draw(app.playerImg)
    for obstaclePosition in app.obstaclePositions:
        x,y = obstaclePosition
        drawImage(CMUImage(app.obstacleImg),x,y)

def main():
    runApp(width=WIDTH, height=HEIGHT)

if __name__ == '__main__':
    main()
