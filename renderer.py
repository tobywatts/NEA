import pygame
import button

from settings import *


class Renderer:
    def __init__(self):

        self.win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Level Editor')

        # load images
        self.background_image = pygame.image.load('bg_images/temp_bg.png').convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.scroll_x = 0
        self.scroll_y = 0

        self.button_column = 0
        self.button_row = 0
        self.tile_button = None

        self.save_image = pygame.image.load('save_button.png')
        self.save_button = button.Button(SCREEN_WIDTH + 100, 565, self.save_image, 1)
        
        self.rect = []

    def draw_bg(self):
        self.win.fill((51, 51, 51))
        width = self.background_image.get_width()
        height = self.background_image.get_height()
        for i in range(2):
            self.win.blit(self.background_image, (i * width - self.scroll_x, 0 - self.scroll_y))
            # will draw images below creating an extra layer below to the background
            self.win.blit(self.background_image, (i * width - self.scroll_x, height - self.scroll_y))

    def draw_world(self,renderer, eventManager):
        for y, row in enumerate(world_data):

            for x, tile in enumerate(row):

                if tile >= 0:

                    eventManager.tiles[tile] = pygame.transform.scale(eventManager.tiles[tile], (TILE_SIZE, TILE_SIZE))
                    self.win.blit(eventManager.tiles[tile], (x * TILE_SIZE - self.scroll_x, y * TILE_SIZE - self.scroll_y))

                    pygame.draw.rect(renderer.win, (255, 255, 255), eventManager.rect[tile], 2)
