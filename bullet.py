import pygame

from settings import *


class Bullet:

    def __init__(self, x, y):
        # laser position
        self.x = x 
        self.y = y
        self.vel = 1500

        # loads the sprites
        self.sprite = pygame.image.load("player_sprites/bullet_img.png")
        self.sprite = pygame.transform.scale(self.sprite, (32, 32))

        self.bullets = []
    
    def show(self, renderer):
        # draws the laser to the screen each frame
        renderer.win.blit(self.sprite, (self.x, self.y))

    def move(self, delta_time):

        # updates the position of the laser each frame
        self.x += self.vel * delta_time
        self.y += self.vel * delta_time