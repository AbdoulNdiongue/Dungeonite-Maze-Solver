from cmu_graphics import *
from settings import *
from PIL import Image

def onAppStart(app):
    app.map = WORLD_MAP

    # Create the Images
    app.player = Image.new('RGB', (TILESIZE, TILESIZE), (0,255,255))
    app.obstacle = Image.new('RGB', (TILESIZE, TILESIZE), (255,0,255))

    #Find positions to draw the player and obstacles
    app.obstaclePositions = []
    app.playerPosition = None

    for row_index, row in enumerate(WORLD_MAP):
        for col_index, val in enumerate(row):

            # setting x and y starting positions for each tile in the world map.
            x = row_index * TILESIZE 
            y = col_index * TILESIZE
            if val == 'x':
                app.obstaclePositions += [(x,y)]
            elif val == 'p':
                app.playerPosition = (x,y)

    #Player
    app.playerSpeed = 10
    app.directionX = 0
    app.directionY = 0





def onKeyPress(app,key):

    #moves player once keys are pressed
    if key == 'right':
        app.directionX = 1
    elif key == 'left':
        app.directionX = -1
    elif key == 'up':
        app.directionY = -1
    elif key == 'down':
        app.directionY = 1

def onKeyRelease(app,key):

    #Stops player's movement once keys are released
    if key == 'right':
        app.directionX = 0
    elif key == 'left':
        app.directionX = 0   
    elif key == 'up':
        app.directionY = 0
    elif key == 'down':
        app.directionY = 0
    
#not working as intended. Appears to lock in just on obstacle, the top left, and uses that for reference. 
def isColliding(playerPosition, obstaclePositions):

    playerX, playerY = playerPosition
    #print(obstaclePositions)
    for obstaclePosition in obstaclePositions:
        obstacleX, obstacleY = obstaclePosition
        
        #print(obstaclePosition)
        #print(f"differenceX: {abs(obstacleX-playerX)}, differenceY:{abs(obstacleY-playerY)}")
        if abs(obstacleX-playerX) <= TILESIZE and abs(obstacleY-playerY) <= TILESIZE:
                return True
        else:
            return False

def onStep(app):

    if app.directionX !=0:
        pass #figure out how to make it so that the character doesnt move faster diagonally

    #Updates the player's position based on the direction its going
    playerX, playerY = app.playerPosition
    playerX += app.directionX * app.playerSpeed
    playerY += app.directionY * app.playerSpeed
    possiblePosition = playerX,playerY
    
    #collision Check 
    print(app.obstaclePositions)
    if isColliding(possiblePosition, app.obstaclePositions) == False:
        app.playerPosition = possiblePosition
        

    
    

def redrawAll(app):

    for position in app.obstaclePositions:
        x,y = position
        drawImage(CMUImage(app.obstacle),x,y)
    x,y = app.playerPosition
    drawImage(CMUImage(app.player),x,y)    

def main():
    runApp(width=WIDTH, height=HEIGHT)

if __name__ == '__main__':
    main()
