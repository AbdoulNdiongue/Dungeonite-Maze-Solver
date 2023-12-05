from cmu_graphics import *
from settings import *
from player import *
from room import *
from PIL import Image

def onAppStart(app):   
    app.mode = 'spawn'
    app.room = Room(SPAWN_ROOM)
    app.keys = set()

    # Create the Images
    app.playerImg = Image.open("graphics/player/down_idle/idle_down.png")
    app.obstacleImg = Image.open("graphics/objects/09.png")
    app.obstacleImg = app.obstacleImg.resize((TILESIZE,TILESIZE))
    app.keyImg = Image.open("graphics/weapons/axe/up.png")
    app.mazeImg = Image.new('RGB', (TILESIZE, TILESIZE), (0,0,0))

    #Find positions to draw the player and obstacles
    app.playerPosition = ((WIDTH//TILESIZE)*TILESIZE/2, (HEIGHT//TILESIZE)*TILESIZE/2) #places player in the middle of the screen 

    #Room
    app.room.roomSetup()
    #Player
    app.player = Player()

def onKeyPress(app,key):
    app.player.move(key)
    
def onKeyRelease(app,key):
    app.player.stopMove(key)

def onStep(app):
    app.player.step(app.room.obstaclePositions)
    
    #print(app.mode, app.keys)

def redrawAll(app):
    app.room.draw(app.obstacleImg)
    drawRect(0,0,300,200,opacity = 50)
    drawLabel('Inventory',150,50, fill = 'white', size = 50)
    app.player.draw(app.playerImg)
    

def main():
     runApp(width=WIDTH, height=HEIGHT)

if __name__ == '__main__':
    main()
