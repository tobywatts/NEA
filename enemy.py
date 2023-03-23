import pygame

from settings import *
from random import choice


class Enemy:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 75
        self.enemy_count = 3
        self.enemy_spawn_locations = [(100, 245), (300, 300,), (450, 170)]
        self.random_spawn = []

    def load_enemies(self):


        for i in range(self.enemy_count):
            temp = choice(self.enemy_spawn_locations)

            if temp not in self.random_spawn:
                self.random_spawn.append(temp)
            
            else:
                self.random_spawn.append(choice(self.enemy_spawn_locations))

            print(self.random_spawn)


    def draw(self, renderer):

        for j in range(len(self.random_spawn)):
            pygame.draw.rect(renderer.win, (255, 0, 0), (self.x + self.random_spawn[j][0] - renderer.scroll_x, 
                                                            self.y + self.random_spawn[j][1] - renderer.scroll_y, self.width, self.height))

    def move(self, player, delta_time):
        if (self.x + self.random_spawn[0][0]) - (player.new_x) <= 100:
            self.x += 100 * delta_time
            

    def shoot(self):
        pass