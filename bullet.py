import pygame

from settings import *


class Bullet:

    def __init__(self, x, y, direction_vect, angle):
        # laser position
        self.x = x 
        self.y = y
        self.vel = 650
        self.direction_vect = direction_vect
        # loads the sprites
        self.sprite = pygame.image.load("player_sprites/bullet_img.png")
        #self.sprite = pygame.transform.scale(self.sprite, (32, 16))
        # calculates the rotation of the laser
        up = pygame.Vector2(1,0)
        angle = up.angle_to(self.direction_vect)
        self.sprite = pygame.transform.rotate(self.sprite, -angle)
    
    def show(self, renderer):
        # draws the laser to the screen each frame
        renderer.win.blit(self.sprite, (self.x-renderer.scroll_x, self.y-renderer.scroll_y))

    def move(self, deltaTime, eventManager):
        # returns vector of same direction but length equal to one 
        temp = self.direction_vect.normalize()  
        # updates the position of the laser each frame

        newPosition = pygame.Vector2(self.x, self.y) + temp * deltaTime * self.vel
        newRect = pygame.Rect(newPosition.x, newPosition.y, 32, 16)
        for hitbox in eventManager.hitboxes:
            if newRect.colliderect(hitbox):
                return self

        self.x = newPosition.x
        self.y = newPosition.y
        return None

