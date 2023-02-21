import pygame
import csv

from settings import *


class EventManager:
    def __init__(self):
        self.running = True

        self.x = 0
        self.y = 0
        self.tiles = []
        self.tile_set = pygame.image.load('tiles/Forest.png')

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def store_tiles(self):
        for i in range(TILE_ROWS * TILE_COLUMNS):
            self.x = i % TILE_ROWS
            self.y = i // TILE_COLUMNS
            tile = self.tile_set.subsurface((self.x * SPRITE_WIDTH, self.y * SPRITE_WIDTH),
                                            (SPRITE_WIDTH, SPRITE_WIDTH))
            self.tiles.append(tile)

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
