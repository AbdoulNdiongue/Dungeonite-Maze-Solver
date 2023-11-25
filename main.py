from cmu_graphics import *
from settings import *
from level import *

class Game:
    def __init__(self):
        self.level = Level()

    def run(self):
        self.level.run()
        runApp(width=WIDTH, height=HEIGHT)

if __name__ == '__main__':
    game = Game()
    game.run()
