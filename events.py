import pygame
import csv

from settings import *


class EventManager:
    def __init__(self, x, y):
        self.running = True

        self.x = x
        self.y = y
        self.tiles = []
        self.rect = []
        self.tile_set = pygame.image.load('tiles/Forest.png')
        self.hitboxes = []
        self.enemy_hitboxes = []
        

    def check_events(self, player, renderer):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player.shoot = True
                player.show_bullet(renderer)
                

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                player.shoot = False
                player.show_bullet(renderer)


    def store_tiles(self):
        for i in range(TILE_ROWS * TILE_COLUMNS):
            self.x = i % TILE_ROWS
            self.y = i // TILE_COLUMNS
            tile = self.tile_set.subsurface((self.x * SPRITE_WIDTH, self.y * SPRITE_WIDTH),
                                            (SPRITE_WIDTH, SPRITE_WIDTH))
            tile_rect = tile.get_rect()
            self.tiles.append(tile)
            self.rect.append(tile_rect)

    def world(self):
        for row in range(2 * ROWS):
            r = [-1] * MAX_COLUMNS
            world_data.append(r)

    def load_level(self, renderer):
        renderer.scroll_x = 0
        with open('level_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    world_data[x][y] = int(tile)

        with open('hitbox_data.txt', 'r') as f:
            line = f.readline()
            while line:
                values = line.strip().split(',')
                left = int(values[0])
                top = int(values[1])
                width = int(values[2])
                height = int(values[3])
                new_hitbox = pygame.Rect(left, top, width, height)
                self.hitboxes.append(new_hitbox)
                line = f.readline()

        with open('enemy_hitbox_data.txt', 'r') as f:
            line = f.readline()
            while line:
                values = line.strip().split(',')
                left = int(values[0])
                top = int(values[1])
                width = int(values[2])
                height = int(values[3])
                new_enemy_hitbox = pygame.Rect(left, top, width, height)
                self.enemy_hitboxes.append(new_enemy_hitbox)
                line = f.readline()
                                      