from cmu_graphics import *
from PIL import Image, ImageDraw
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        #sprite group settup
        self.visible_sprites = [] #fill in with whatever grouping method cmu_graphics has
        self.obstacle_sprites = []

        #sprite setup
        self.create_map()
        
    def create_map(self): #Stuck at loading the images, need help.
        self.image = Image.open('../level_graphics/graphics/test/rock.png')
        self.visible_sprites.append(self.image)
        
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):

                # setting x and y starting positions for each tile in the world map.
                self.x = row_index * TILESIZE 
                self.y = col_index * TILESIZE

                # creating classes for obstacles and player
                if col == 'x':
                    Tile((self.x,self.y), self.visible_sprites)
                elif col == 'p':
                    Player((self.x,self.y), self.visible_sprites)


    def run(self):
        #update and draw the game

        #using animation with lists, draw all sprites in self.visible sprites 
        def appStarted(app):
            app.x = self.x
            app.y = self.y
            
        def redrawAll(app,canvas):
            for sprite in self.visible_sprites:
                drawImage(sprite, app.x, app.y, align = 'center')
