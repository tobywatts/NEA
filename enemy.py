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
        self.temp_enemies = []
        self.enemies = []
    def load_enemies(self, renderer):


        for i in range(self.enemy_count):
            temp = choice(self.enemy_spawn_locations)

            if temp not in self.random_spawn:
                self.random_spawn.append(temp)
            
            else:
                self.random_spawn.append(choice(self.enemy_spawn_locations))

        for i in range(len(self.random_spawn)):
            self.temp_enemies.append(pygame.Rect(self.random_spawn[i][0], self.random_spawn[i][1], self.width, self.height))

            print(self.random_spawn)


    def draw(self, renderer):

        for i in range(len(self.random_spawn)):
            temp_enemy = self.temp_enemies[i]  
            offset_enemy = pygame.Rect(temp_enemy.x - renderer.scroll_x, temp_enemy.y - renderer.scroll_y, temp_enemy.width, temp_enemy.height)
            self.enemies.append(offset_enemy)

        # for enemy in self.enemies:
            pygame.draw.rect(renderer.win, (255, 0, 0), offset_enemy)

    def move(self, player, delta_time):
        for enemy in self.enemies:
            if enemy.x - player.new_x <= 100:
                enemy.x += 100 * delta_time
        # if (self.x + self.random_spawn[0][0]) - (player.new_x) <= 100:
        #     self.x += 100 * delta_time
            

    def shoot(self):
        pass