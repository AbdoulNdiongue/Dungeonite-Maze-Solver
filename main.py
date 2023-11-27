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
    app.obstaclePositions = []
    app.playerPosition = None

    for row_index, row in enumerate(WORLD_MAP):
        for col_index, val in enumerate(row):

            # setting x and y starting positions for each tile in the world map.
            x = col_index * TILESIZE 
            y = row_index * TILESIZE
            if val == 'x':
                app.obstaclePositions += [(x,y)]
            elif val == 'p':
                app.playerPosition = (x,y)

    #Player
    app.player = Player(app.playerPosition)

    #Obstacles 
    app.obstacles = Obstacles(app.obstaclePositions)

def onKeyPress(app,key):
    app.player.move(key)
    
def onKeyRelease(app,key):
    app.player.stopMove(key)

def onStep(app):

    app.player.step(app.obstaclePositions)

def redrawAll(app):
    app.player.draw(app.playerImg)
    app.obstacles.draw(app.obstacleImg)

def main():
    runApp(width=WIDTH, height=HEIGHT)

if __name__ == '__main__':
    main()
