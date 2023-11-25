from cmu_graphics import *
from settings import *

class Tile(): #sprite is the input
    def __init__(self, pos, groups):
        #stuck on the step below of trying to print out the images of obstacles. 
        self.image = Image.open('../level graphics/graphics/test/rock.png') #the image of the sprite
        self.rect = self.image #Somehow get the rectangle of the sprite using the position