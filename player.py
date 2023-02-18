import pygame

from settings import *


class Player:

    def __init__(self):
        self.x = 400
        self.y = 320
        self.width = 40
        self.height = 70
        self.vel = 350
        self.jump_vel = 700
        self.health = 100
        self.gravity = 700
        self.isJump = False
        self.jump_height = 1000

    def draw(self, renderer):
        pygame.draw.rect(renderer.win, (255, 255, 255), (self.x, self.y, self.width, self.height))

        # def jump(self, renderer):

        # for i in range(100):
        # Player.draw(self, renderer)

    def move(self, renderer, delta_time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.vel * delta_time

        if keys[pygame.K_d]:
            self.x += self.vel * delta_time

        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            self.y -= self.jump_vel * delta_time

        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            self.isJump = True

        if self.isJump:
            self.y -= self.jump_vel * delta_time
            self.jump_vel -= self.gravity * delta_time

            if self.jump_vel < -self.jump_height:
                self.isJump = False
                self.jump_vel = self.jump_height
                #pygame.draw.rect(renderer.win, (255, 255, 255), (self.x, self.y, self.width, self.height))

        if self.y < 640:
            self.y += self.gravity * delta_time
        if self.y > 500:
            self.y = 500
