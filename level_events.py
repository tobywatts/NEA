import pygame
import csv

from level_settings import *


class EventManager:
    def __init__(self):
        self.running = True

        self.x = 0
        self.y = 0
        self.tiles = []
        self.tile_set = pygame.image.load('tiles/Forest.png')
        self.current_tile = 0
        self.hitboxes = []
        self.hitbox_x = []
        self.hitbox_y = []
        self.hitbox_width = TILE_SIZE

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

    def check_scroll(self, renderer, delta_time):
        keys = pygame.key.get_pressed()
        # scrolling background
        if keys[pygame.K_a] and renderer.scroll_x > 0:  # left
            renderer.scroll_x -= 500 * delta_time

        if keys[pygame.K_d] and renderer.scroll_x < (renderer.background_image.get_width() * 2 - SCREEN_WIDTH):
            renderer.scroll_x += 500 * delta_time

        if keys[pygame.K_w] and renderer.scroll_y > 0:
            renderer.scroll_y -= 500 * delta_time

        if keys[pygame.K_s] and renderer.scroll_y < (2 * renderer.background_image.get_height() - SCREEN_HEIGHT):
            renderer.scroll_y += 500 * delta_time

    def tile_placing(self, renderer):
        pos = pygame.mouse.get_pos()
        x = int((pos[0] + renderer.scroll_x) // TILE_SIZE)
        y = int((pos[1] + renderer.scroll_y) // TILE_SIZE)

        # Check that coordinates are within the tile area
        if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
            # update tile value
            if pygame.mouse.get_pressed()[0] == 1:  # checks for left click
                if world_data[y][x] != self.current_tile:
                    world_data[y][x] = self.current_tile

            if pygame.mouse.get_pressed()[2] == 1:  # checks for right click
                world_data[y][x] = -1


                
    
    def load_level(self, renderer):
        renderer.scroll_x = 0
        with open('level_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    world_data[x][y] = int(tile)

    def save_level(self, renderer):
        if renderer.save_button.draw(renderer.win):
            with open('level_data.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                for row in world_data:
                    writer.writerow(row)
