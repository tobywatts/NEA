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

        renderer.scroll_y = max(0, renderer.scroll_y)
        renderer.scroll_y = min(renderer.background_image.get_height() * 2 - SCREEN_HEIGHT, renderer.scroll_y)
        renderer.scroll_x = max(0, renderer.scroll_x)
        renderer.scroll_x = min(renderer.background_image.get_width() * 2 - SCREEN_WIDTH, renderer.scroll_x)

    def tile_placing(self, renderer):

        keys = pygame.key.get_pressed()

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

            if pygame.mouse.get_pressed()[1] == 1: # checks for middle click
                newHitbox = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                flag = True
                for hitbox in self.hitboxes:
                    if hitbox.colliderect(newHitbox):
                        flag = False
                if flag:
                    self.hitboxes.append(newHitbox)

            if keys[pygame.K_e]:
                for hitbox in self.hitboxes:
                    if hitbox.collidepoint(pos[0] + renderer.scroll_x, pos[1] + renderer.scroll_y):
                        self.hitboxes.remove(hitbox)


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
                                      

    def save_level(self, renderer):
        if renderer.save_button.draw(renderer.win):
            with open('level_data.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                for row in world_data:
                    writer.writerow(row)
                csvfile.close()

            with open('hitbox_data.txt', 'w') as f:
                for item in self.hitboxes:
                    top = item.top
                    left = item.left
                    width = item.width
                    height = item.height
                    f.write(str(left) + ',' + str(top) + ',' + str(width) + ',' + str(height) + '\n')
                f.close()

