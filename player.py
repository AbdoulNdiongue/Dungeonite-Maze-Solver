from cmu_graphics import *
from settings import *

class Player(): #sprite is the input
    def __init__(self, pos, groups):
        self.image = '' #the image of the sprite
        self.rect = '' #the rectangle the sprite takes up... its hitbox