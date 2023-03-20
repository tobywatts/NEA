import pygame

from settings import *


class Player:

    def __init__(self):
        self.x = 400
        self.y = 320
        self.width = 40
        self.height = 70
        self.vel = 350
        self.jump_vel = 750
        self.health = 100
        self.gravity = 775
        self.jump = False
        self.jump_height = 50

    def draw(self, renderer):
        pygame.draw.rect(renderer.win, (255, 255, 255), (self.x, self.y, self.width, self.height))

        # def jump(self, renderer):

        # for i in range(100):
        # Player.draw(self, renderer)

    def move(self, delta_time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.vel * delta_time

        if keys[pygame.K_d]:
            self.x += self.vel * delta_time

        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            self.y -= self.jump_vel * delta_time

        if self.jump is False and keys[pygame.K_SPACE] or keys[pygame.K_w]:
            self.jump = True
        
        if self.jump is True:
            self.y -= self.jump_vel * delta_time
            self.jump_vel -= 1000 * delta_time

            if self.jump_vel < -self.jump_height * delta_time:
                self.jump = False
                self.jump_vel = 750

        if self.y < 640:
            self.y += self.gravity * delta_time
        if self.y > 500:
            self.y = 500

        if self.x < 0:
            self.x = 0
