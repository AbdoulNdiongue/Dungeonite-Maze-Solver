from cmu_graphics import *
from settings import *
from player import *
from room import *
from PIL import Image

def onAppStart(app):   
    app.mode = 'spawn'
    app.room = Room(SPAWN_ROOM)
    app.keys = set()
    app.onStepCounter = 0
    app.timer = 179
    # Create the Images
    app.playerImg = Image.open("graphics/player/down_idle/idle_down.png")
    app.obstacleImg = Image.open("graphics/objects/09.png")
    app.obstacleImg = app.obstacleImg.resize((TILESIZE,TILESIZE))
    app.keyImg = Image.open("graphics/weapons/axe/down.png")
    app.keyImg.resize((TILESIZE,TILESIZE))
    app.mapImg = Image.new('RGB',(WIDTH,HEIGHT), (80,80,80))

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
    app.onStepCounter += 1
    app.player.step(app.room.obstaclePositions)
    if app.onStepCounter % 60 == 0:
        app.timer -= 1
    
    #print(app.mode, app.keys)

def redrawAll(app):
    if app.timer > 0:
        drawImage(CMUImage(app.mapImg),0,0)
        app.room.draw(app.obstacleImg)
        drawRect(0,0,250,150,opacity = 50)
        drawLabel('Inventory',125,50, fill = 'white', size = 50)
        drawRect(0,570,250,100,opacity = 50)
        drawLabel('Time Remaining:',125,600, fill = 'white', size = 32)
        drawLabel(f'{app.timer}s', 125,640, size = 35, fill = 'white')
        app.player.draw(app.playerImg)
    else:
        drawRect(0,0,WIDTH,HEIGHT,opacity = 100)
    

def main():
     runApp(width=WIDTH, height=HEIGHT)

if __name__ == '__main__':
    main()
