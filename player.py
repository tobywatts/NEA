import pygame

from settings import *


class Player:

    def __init__(self):
        self.x = 400
        self.y = 320
        self.width = 40
        self.height = 70
        self.vel = 350
        self.jump_vel = 0
        self.jump_height = 725
        self.health = 100
        self.gravity = 1500
        self.jump = False
        self.onGround = True

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        

    def draw(self, renderer):
        pygame.draw.rect(renderer.win, (255, 255, 255), (self.x - renderer.scroll_x, self.y - renderer.scroll_y, self.width, self.height))
        self.hitbox = pygame.Rect(self.x - renderer.scroll_x, self.y - renderer.scroll_y, self.width, self.height)

    def move(self, eventManager, renderer, delta_time):
        keys = pygame.key.get_pressed()
        newPosition = pygame.Vector2(self.x, self.y)

        if keys[pygame.K_a]:
            newPosition.x -= self.vel * delta_time

        if keys[pygame.K_d]:
            newPosition.x += self.vel * delta_time

        if self.onGround and (keys[pygame.K_SPACE] or keys[pygame.K_w]):
            # jump
            self.jump_vel = -self.jump_height
            self.onGround = False
        
        if not self.onGround:
            self.jump_vel += self.gravity * delta_time 
            self.jump_vel = min(1000, self.jump_vel)
        newPosition.y += self.jump_vel * delta_time
        
        
        newHitboxX = pygame.Rect(newPosition.x, self.y, self.width, self.height)
        newHitboxY = pygame.Rect(self.x, newPosition.y, self.width, self.height)

        canMoveX = True
        for hitbox in eventManager.hitboxes:
            if hitbox.colliderect(newHitboxX):
                canMoveX = False
                break
        if canMoveX:
            self.x = newPosition.x
        
        canMoveY = True
        for hitbox in eventManager.hitboxes:
            if hitbox.colliderect(newHitboxY):
                if newPosition.y < hitbox.y:
                    self.y = hitbox.y - self.height
                    self.onGround = True  
                    self.jump_vel = 0
                canMoveY = False
                break
        if canMoveY:
            self.onGround = False
            self.y = newPosition.y

        renderer.scroll_x = self.x - 400
        renderer.scroll_y = self.y - 320

        renderer.scroll_x = max(0, renderer.scroll_x)
        renderer.scroll_x = min(renderer.scroll_x, 1400)
        renderer.scroll_y = max(0, renderer.scroll_y)
        renderer.scroll_y = min(renderer.scroll_y, 640)
