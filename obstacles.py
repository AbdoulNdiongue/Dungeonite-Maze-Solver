from cmu_graphics import *

class Obstacles():
    def __init__(self, obstaclePositions):
        self.obstaclePositions = obstaclePositions

    def draw(self, obstacleImg):
        for obstaclePosition in self.obstaclePositions:
            x,y = obstaclePosition
            drawImage(CMUImage(obstacleImg),x,y)