import pygame

from settings import *


class Bullet:

    def __init__(self, x, y, directionVect):
        # laser position
        self.x = x 
        self.y = y
        self.vel = 1500
        self.directionVect = directionVect
        # loads the sprites
        self.sprite = pygame.image.load("bullet_img.png")
        self.sprite = pygame.transform.scale(self.sprite, (32, 16))
        # calculates the rotation of the laser
        up = pygame.Vector2(1,0)
        angle = up.angle_to(self.directionVect)
        self.sprite = pygame.transform.rotate(self.sprite, -angle)
        self.bullets = []
    
    def show(self, renderer):
        # draws the laser to the screen each frame
        renderer.win.blit(self.sprite, (self.x, self.y))

    def move(self, deltaTime):
        # returns vector of same direction but length equal to one 
        temp = self.directionVect.normalize()  
        # updates the position of the laser each frame
        self.x += temp.x * deltaTime * self.vel
        self.y += temp.y * deltaTime * self.vel

